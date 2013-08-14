# -*- coding: utf-8 -*-
import sys, os
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'KBS Map Viewer'
version = '1'
release = '1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'kbs-map-viewer'
latex_documents = [
  ('index', 'kbs-map-viewer.tex', u'KBS Map Viewer',
   u'Kansas Biological Survey', 'manual'),
]
man_pages = [
    ('index', 'kbs-map-viewer', u'KBS Map Viewer',
     [u'Kansas Biological Survey'], 1)
]
