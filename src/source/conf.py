# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Loadupch'
copyright = '2024, Unit Electronics'
author = 'Unit Electronics'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx_togglebutton',
    'rst2pdf.pdfbuilder',
]

templates_path = ['_templates']
exclude_patterns = []
master_doc = 'index'
numfig = True

html_theme = 'piccolo_theme'
# html_theme = 'sphinx_material'
# html_theme = 'sphinx_rtd_theme'
html_logo = "_static/Logo-UNIT_Web-04-800x182.png"
html_static_path = ['_static']
latex_logo = "_static/Logo-UNIT_Web-04-800x182.png"
html_css_files = [
    'custom.css',
]