"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options.

References:
  - Full list of documentation:
      https://www.sphinx-doc.org/en/master/usage/configuration.html
  - Autodoc example blog post:
      https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365
"""
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "src")))


# -- Project information -----------------------------------------------------

project = "factorymind"
copyright = "2021, FactoryMind"
author = "FactoryMind"

# The full version, including alpha/beta/rc tags
release = "0.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. Here we use extensions for auto-documentation from the source
# code, see
#  https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# extensions = ["sphinx.ext.autosummary", "sphinx.ext.autodoc"]
extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Extensions that recomonmark will use
source_suffix = {".rst": "restructuredtext", ".txt": "markdown", ".md": "markdown"}

# Auto generate API documentation for modules
autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "nature"
# html_theme = "sphinx_rtd_theme"

# html_theme_options = {
#    "logo": "logo.png",
#    "github_user": "factorymind",
#    "github_repo": "factorymind",
#    # "note_bg": "#FFF59C",
#    "show_powered_by": False,
#    "show_related": True,
#    "sidebar_collapse": True,
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
