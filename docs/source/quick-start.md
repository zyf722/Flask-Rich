# Quick Start

The extension itself offers an out-of-the-box experience, and you can register it with your Flask app within just a few lines of code.

Like any other Flask extension, you can initialize and register Flask-Rich with your Flask app in two ways:

## Single File

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

## Factory Pattern

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

After registering, the `RichApplication` class shall do all the work for you. Just use the Flask {py:attr}`flask.Flask.logger` object to log rich texts.