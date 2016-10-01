#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -- Imports and system paths

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.intersphinx',
]
templates_path = ['_templates']
source_suffix = ['.rst', '.md', '.ipynb']
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'dock-doc'
copyright = '2016, Carol Willing'
author = 'Carol Willing'

version = '0.1'  # short X.Y version
release = '0.1'
language = None

# There are two options for replacing |today|:
# today = ''
# today_fmt = '%B %d, %Y'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# default_role = None
# add_function_parentheses = True
# add_module_names = True
# show_authors = False
pygments_style = 'sphinx'
# modindex_common_prefix = []
# keep_warnings = False
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'alabaster'
# html_theme_options = {}
# html_theme_path = []
# html_title = 'dock-doc v0.1'
# html_short_title = None
# html_logo = None
# html_favicon = None
html_static_path = ['_static']
# html_extra_path = []
# html_last_updated_fmt = None
# html_use_smartypants = True
# html_sidebars = {}
# html_additional_pages = {}
# html_domain_indices = True
# html_use_index = True
# html_split_index = False
# html_show_sourcelink = True
# html_show_sphinx = True
# html_show_copyright = True
# html_use_opensearch = ''
# html_file_suffix = None
# html_search_language = 'en'
# html_search_options = {'type': 'default'}
# html_search_scorer = 'scorer.js'
htmlhelp_basename = 'dock-docdoc'


# -- Options for LaTeX output --------------------------

latex_elements = {
     # 'papersize': 'letterpaper',
     # 'pointsize': '10pt',
     # 'preamble': '',
     # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'dock-doc.tex', 'dock-doc Documentation',
     'Carol Willing', 'manual'),
]
# latex_logo = None
# latex_use_parts = False
# latex_show_pagerefs = False
# latex_show_urls = False
# latex_appendices = []
# latex_keep_old_macro_names = True
# latex_domain_indices = True


# -- Options for manual page output -------------------

man_pages = [
    (master_doc, 'dock-doc', 'dock-doc Documentation',
     [author], 1)
]
# man_show_urls = False


# -- Options for Texinfo output -------------------

texinfo_documents = [
    (master_doc, 'dock-doc', 'dock-doc Documentation',
     author, 'dock-doc', 'One line description of project.',
     'Miscellaneous'),
]

# texinfo_appendices = []
# texinfo_domain_indices = True
# texinfo_show_urls = 'footnote'
# texinfo_no_detailmenu = False


# -- Intersphinx --------------------------------

intersphinx_mapping = {'https://docs.python.org/': None}

# -- Read The Docs check ------------------------
