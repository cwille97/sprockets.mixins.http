#!/usr/bin/env python
import sphinx_rtd_theme
from sprockets.mixins import http

needs_sphinx = '1.0'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'sprockets.mixins.http'
author = 'AWeber Communications'
copyright = '2017-2020, AWeber Communications'
version = http.__version__
release = '.'.join(version.split('.')[:-1])
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'tornado': ('https://www.tornadoweb.org/en/stable/', None),
}
