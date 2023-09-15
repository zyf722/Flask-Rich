# Configuration

## Custom Parameters

Check {doc}`reference` for more information in this section.

## Config Options

Flask-Rich gets its configuration from application's config, which can be set in multiple ways.

All options have the `RICH_` prefix and can be found below.

### `RICH_HIGHLIGHTING: bool = True`

Whether to enable Rich's {doc}`rich:highlighting` in logging.

### `RICH_HIGHLIGHTING_KEYWORDS: tuple[str, ...] = ()`

A tuple of keywords to highlight in logging, only takes effect when `RICH_HIGHLIGHTING` is {py:data}`True`.

### `RICH_LOGGING: bool = True`

Whether to use Rich's {doc}`rich:logging`.

### `RICH_LOGGING_MARKUP: bool = True`

Whether to allow Rich's {doc}`rich:markup` format in logging.

An example of console markup is `[blue]Hello[/blue], world!`.

### `RICH_TRACEBACK: bool = True`

Whether to use Rich's {doc}`rich:traceback` handler.

### `RICH_TRACEBACK_EXTRA_LINES: int = 1`

When Rich prints the lines of code which raised the error, how many lines around it does it print as well. In the library it defaults to 3, but 1 is better for web applications.

### `RICH_TRACEBACK_SHOW_LOCALS: bool = False`

Whether to print the local variables with traceback.

### `RICH_TRACEBACK_SUPPRESS: Sequence[Union[str, ModuleType]] = (flask, )`

A sequence of modules to suppress from the traceback. By default, it suppresses {py:mod}`flask`.

### `RICH_ROUTES: bool = True`

Whether to add a new command `rich-routes` that uses Rich's {doc}`rich:tables` to show all routes. 

### `RICH_ROUTES_MODE: str = Literal["table"]`

What mode the command `rich-routes` is in. Currently there is only one option: `table`.
