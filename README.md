> [!NOTE]
> **This repository is an official fork of the original [BD103/Flask-Rich](https://github.com/BD103/Flask-Rich) project.** All releases after 0.3 will be published from this fork.
---

[![License](https://img.shields.io/github/license/zyf722/Flask-Rich)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/flask-rich
)](https://pypi.org/project/flask-rich/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-rich)
[![Documentation Status](https://readthedocs.org/projects/flask-rich/badge/?version=latest)](https://flask-rich.readthedocs.io/en/latest/?badge=latest)


# Flask-Rich

Flask-Rich is a Flask extension that implements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/), which brings better logging / tracebacks with *rich* text formatting, and more features related to the console.

[![asciicast](https://asciinema.org/a/608190.svg)](https://asciinema.org/a/608190)

## Features

- :rainbow: Better console logging powered by [Rich's logging](https://rich.readthedocs.io/en/latest/logging.html) handler, with full support for [console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup), [highlighting](https://rich.readthedocs.io/en/latest/highlighting.html),  [tracebacks](https://rich.readthedocs.io/en/latest/traceback.html) and more
- :construction: Builtin support for [Werkzeug](https://pypi.org/project/Werkzeug/) which runs the Flask development server
- :mag: A new `rich-routes` Flask command that use Rich to show all routes
- :wrench: Customizable and toggleable features


## Basic Usage

Just like any other Flask extension, you can initialize and register Flask-Rich with your Flask app in two ways:

### Single File

```python
from flask import Flask
from flask_rich import RichApplication

class Config:
    RICH_LOGGING = True

app = Flask(__name__)
app.config.from_object(Config())  # or any other way to load config

# Initialize the extension with the app
rich = RichApplication(app)

@app.route("/")
def index():
    return "Hello World!"
```

### Factory Pattern

```python
# rich.py
from flask_rich import RichApplication

# Initialize the extension without an app
rich = RichApplication()
```

```python
# app.py
from flask import Flask
from .rich import rich

class Config:
    RICH_LOGGING = True

def create_app:
    app = Flask(__name__)
    app.config.from_object(Config())  # or any other way to load config

    # Register the extension with the app
    rich.init_app(app)
    # ...
    return app
```

After registering, the `RichApplication` class shall do all the work for you.

You can now use the `app.logger` object to log rich text, and use the `flask rich-routes` command to show all routes.

For further usage and configuration, please refer to the [documentation](https://flask-rich.readthedocs.io/en/latest/).

## Feedback

If you have any suggestions or troubles using this extension, please feel free to open an [issue](https://github.com/zyf722/Flask-Rich/issues).

## Contributing

[Pull Requests](https://github.com/zyf722/Flask-Rich/pulls) are welcome!

You can setup your own copy of the source code with Git and [Poetry](https://python-poetry.org/):

```shell
# Git
git clone https://github.com/zyf722/Flask-Rich.git
cd Flask-Rich/

# Poetry
poetry lock
poetry install
poetry shell
```

It is strongly recommended to follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification when writing commit messages and creating pull requests.

## Credits
Thanks to the following people for their contributions:
- [BD103](https://github.com/BD103) for creating the original project and maintaining it until version `0.3.1`
- [Will McGugan](https://github.com/willmcgugan) and all other contributors of the [Rich](https://github.com/Textualize/rich) project
- [Pallets](https://github.com/pallets) and all other contributors of the [Flask](https://github.com/pallets/flask) project