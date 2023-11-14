# Flask-Rich

Flask-Rich is a Flask extension that implements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/), which brings better logging / tracebacks with *rich* text formatting, and more features related to the console.

[![asciicast](https://asciinema.org/a/608190.svg)](https://asciinema.org/a/608190)

## Features

- Better console logging powered by [Rich's logging](https://rich.readthedocs.io/en/latest/logging.html) handler, with full support for [console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup), [highlighting](https://rich.readthedocs.io/en/latest/highlighting.html),  [tracebacks](https://rich.readthedocs.io/en/latest/traceback.html) and more
- Builtin support for [Werkzeug](https://pypi.org/project/Werkzeug/) which runs the Flask development server
- A new `rich-routes` Flask command that use Rich to show all routes
- Customizable and toggleable features

```{eval-rst}
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation.md
   quick-start.md
   configuration.md
   flask-commands.md
   reference.md
   changelog.md
```