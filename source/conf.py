import os
import sys

project = 'GIS con Python'
copyright = '2026, GISLAB | CICIMAR-IPN'
author = 'Programas de Posgrado'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'myst_nb', # Reemplaza a myst-parser y permite la integración de notebooks en Sphinx
]

# Opciones de ejecución de notebooks disponibles: "off", "auto", "force", "cache"
nb__execution_mode = 'off'

# Formatos reconocidos como fuentes de documentación
source_suffix = { '.rst': 'restructuredtext', '.ipynb': 'myst-nb', '.myst': 'myst-nb', }

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
