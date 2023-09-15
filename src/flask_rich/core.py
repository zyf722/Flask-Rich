import logging

import click
import flask
from flask.logging import default_handler
from ochre.spaces import RGB, Ansi256
from rich.color import ANSI_COLOR_NAMES
from rich.console import Console
from rich.highlighter import Highlighter, NullHighlighter
from rich.logging import RichHandler
from rich.markup import escape as escape_markup
from rich.table import Column, Table
from stransi import Ansi
from stransi.attribute import SetAttribute
from stransi.color import ColorRole, SetColor


class RichApplication:
    """
    A Flask extension that adds rich logging features to the application.
    """

    def __init__(
        self,
        app: flask.Flask = None,
        console: Console = None,
        highlighter: Highlighter = None,
    ):
        """
        Args:
            app:
                The Flask Application object.
            console:
                A `rich.console.Console` instance to use for logging. Defaults to a new `Console` instance.
            highlighter:
                A `rich.highlighter.Highlighter` instance to use for logging. Defaults to :py:data:`None`, which will use an instance of :class:`rich:rich.highlighter.ReprHighlighter` internally in :class:`rich:rich.logging.RichHandler`.
        """
        self.app = app

        if app is not None:
            self.init_app(app, console, highlighter)

    def init_app(
        self,
        app: flask.Flask,
        console: Console = None,
        highlighter: Highlighter = None,
    ):
        """
        Register this extension with the flask app.

        Args:
            app:
                The Flask Application object.
            console:
                A `rich.console.Console` instance to use for logging. Defaults to a new `Console` instance.
            highlighter:
                A `rich.highlighter.Highlighter` instance to use for logging. Defaults to :py:data:`None`, which will use an instance of :class:`rich:rich.highlighter.ReprHighlighter` internally in :class:`rich:rich.logging.RichHandler`.
        """
        if console is None:
            self.console = Console()

        defaults = [
            ("RICH_HIGHLIGHTING", True),
            ("RICH_HIGHLIGHTING_KEYWORDS", ()),
            ("RICH_LOGGING", True),
            ("RICH_LOGGING_MARKUP", True),
            ("RICH_TRACEBACK", True),
            ("RICH_TRACEBACK_EXTRA_LINES", 1),
            ("RICH_TRACEBACK_SHOW_LOCALS", False),
            ("RICH_TRACEBACK_SUPPRESS", (flask,)),
            ("RICH_ROUTES", True),
            ("RICH_ROUTES_MODE", "table"),
        ]

        for k, v in defaults:
            app.config.setdefault(k, v)

        if app.config["RICH_LOGGING"]:

            class FlaskRichHandler(RichHandler):
                """
                A extended RichHandler that converts ANSI markup to Rich markup.
                """

                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.attribute_map = {
                        0: "default on default not bold not dim not italic not underline not blink not reverse",
                        1: "bold",
                        2: "dim",
                        3: "italic",
                        4: "underline",
                        5: "blink",
                        7: "reverse",
                    }
                    self.ansi256_color_map = {v: k for k, v in ANSI_COLOR_NAMES.items()}

                def emit(self, record):
                    message = record.msg % record.args
                    record.args = ()

                    escaped_message = (
                        message
                        if app.config["RICH_LOGGING_MARKUP"]
                        else escape_markup(message)
                    )
                    record.msg = self.convert_ansi(escaped_message)

                    super().emit(record)

                def convert_ansi(self, message):
                    """
                    Convert ANSI markup to Rich markup.
                    """
                    message_ansi = Ansi(message)
                    ret = ""
                    for item in list(message_ansi.instructions()):
                        if isinstance(item, str):
                            ret += item
                        elif isinstance(item, SetColor):
                            color = item.color
                            if isinstance(color, Ansi256):
                                color_markup = (
                                    f"{self.ansi256_color_map[color.ansi256.code]}"
                                )
                            elif isinstance(color, RGB):
                                color_markup = f"#{hex(color.hex.hex_code)[2:]}"
                            ret += f"[{'on ' if item.role == ColorRole.BACKGROUND else ''}{color_markup}]"
                        elif isinstance(item, SetAttribute):
                            if item.attribute.value in self.attribute_map:
                                ret += f"[{self.attribute_map[item.attribute.value]}]"
                    return ret

            if not app.config["RICH_HIGHLIGHTING"]:
                highlighter = NullHighlighter()

            rich_handler = FlaskRichHandler(
                markup=True,  # Hardcoded to True, since we're converting ANSI markup to Rich markup
                highlighter=highlighter,
                rich_tracebacks=app.config["RICH_TRACEBACK"],
                tracebacks_extra_lines=app.config["RICH_TRACEBACK_EXTRA_LINES"],
                tracebacks_show_locals=app.config["RICH_TRACEBACK_SHOW_LOCALS"],
                tracebacks_suppress=app.config["RICH_TRACEBACK_SUPPRESS"],
                # Prevent Rich from using its default keywords
                keywords=app.config["RICH_HIGHLIGHTING_KEYWORDS"],
            )

            app.logger.removeHandler(default_handler)
            app.logger.addHandler(rich_handler)

            # Support for Werkzeug's logger
            logging.getLogger("werkzeug").addHandler(rich_handler)

        if app.config["RICH_ROUTES"]:
            if app.config["RICH_ROUTES_MODE"] == "table":

                @app.cli.command(
                    "rich-routes", short_help="Show the routes for the app."
                )
                @click.option(
                    "--all-methods", is_flag=True, help="Show HEAD and OPTIONS methods."
                )
                def rich_routes_command(all_methods: bool) -> None:
                    rules = list(app.url_map.iter_rules())

                    if not rules:
                        click.echo("No routes were registered.")
                        return

                    ignored_methods = set(() if all_methods else ("HEAD", "OPTIONS"))

                    rule_methods = [
                        ", ".join(sorted(rule.methods - ignored_methods))  # type: ignore
                        for rule in rules
                    ]

                    table = Table(
                        Column("Endpoint", style="bright_magenta"),
                        Column("Methods", style="cyan"),
                        Column("Rule", style="green"),
                        title="App Routes",
                    )

                    for rule, methods in zip(rules, rule_methods):
                        table.add_row(rule.endpoint, methods, rule.rule)

                    self.console.print(table)
