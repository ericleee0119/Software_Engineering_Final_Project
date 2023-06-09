# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os 
import sys 
sys.path.insert(0, os.path.abspath('../../src/Software_Engineering_Final_Project'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Crime Map'
copyright = '2023, Kuan-Lin, Chan-Yu, Li-Yeh, Mengqiao'
author = 'Kuan-Lin, Chan-Yu, Li-Yeh, Mengqiao'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','autoapi.extension']
autoapi_type = 'python'
autoapi_dirs = os.path.abspath('../../src/Software_Engineering_Final_Project')
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
