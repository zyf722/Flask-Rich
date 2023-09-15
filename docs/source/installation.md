# Installation

## Requirements
This extension requires Python 3.8 or higher, with a terminal that supports ANSI escape sequences.

## Pip
The easiest way to install this extension is through pip:
```bash
pip install flask-rich
```

To upgrade, use:
```bash
pip install --upgrade flask-rich
```

## Poetry
It is recommended to use [Poetry](https://python-poetry.org/) to manage your project's dependencies and virtual environment.

To install this extension with Poetry, use:
```bash
poetry add flask-rich
```

## From Source
If you prefer to install from source, you need to clone this repository and install the dependencies with Poetry:

```bash
git clone https://github.com/zyf722/Flask-Rich.git
cd Flask-Rich/

poetry lock
poetry install
poetry shell
```

You can also build the source distribution and install it with pip:

```bash
poetry build
cd dist/
# Replace *.*.* with the version number
pip install -U Flask_Rich-*.*.*-py3-none-any.whl
```