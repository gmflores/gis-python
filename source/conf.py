import os
import sys

project = 'Cartografia y Analisis Espacial con Python para Ciencias Marinas'
copyright = '2026, Maestria en Ciencias Marinas'
author = 'Programa de Posgrado en Ciencias Marinas'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'es'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}
