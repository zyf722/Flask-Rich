# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import pkg_resources
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Flask-Rich"
copyright = "BD103, zyf722"
author = "BD103, zyf722"
release = pkg_resources.get_distribution("flask_rich").version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "sphinx_rtd_theme"

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "flask": ("https://flask.palletsprojects.com/en/3.0.x/", None),
    "rich": ("https://rich.readthedocs.io/en/latest", None),
    "werkzeug": ("https://werkzeug.palletsprojects.com/en/3.0.x/", None),
}

autodoc_typehints = "description"

autoclass_content = "both"

html_static_path = [sphinx_rtd_theme.get_html_theme_path()]
