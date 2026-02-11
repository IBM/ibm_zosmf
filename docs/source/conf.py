##############################################################################
# © Copyright IBM Corporation 2020, 2026                                     #
##############################################################################

##############################################################################
#                 Sphinx documentation Configuration                         #
##############################################################################
# Configuration file for the Sphinx documentation builder, for more follow link:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# ``sphinx-build``` options follow link:
# https://www.sphinx-doc.org/en/latest/man/sphinx-build.html
##############################################################################

##############################################################################
# Project information
##############################################################################

project = 'IBM z/OS core collection'
copyright = '2026, IBM'
author = 'IBM'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# Disable the Copyright footer for Read the docs at the bottom of the page
# by setting property html_show_copyright = False
html_show_copyright = True

# Disable showing Sphinx footer message:
# "Built with Sphinx using a theme provided by Read the Docs. "
html_show_sphinx = False

##############################################################################
# General configuration
##############################################################################

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx_rtd_theme",
    'sphinx_copybutton',
    "sphinx_design"
]

# Add any paths that contain templates here, relative to this directory.
# This sites template is ../templates/module.rst.j2
templates_path = ['../templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['requirements.rst', 'requirements_managed.rst']

##############################################################################
# Options for HTML output
##############################################################################

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes such 'alabaster'. Currently this site uses the
# sphinx_rtd_theme HTML theme.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the built-in "default.css".
# html_static_path = ['_static']


def setup(app):
    app.add_css_file('my_theme.css')


html_static_path = ['_static']

html_css_files = [
    'css/table.css',
    'css/custom.css'
]

# Github options used with Sphinx
html_context = {
    "display_github": "True",
    "github_user": "ansible-collections",
    "github_repo": "ibm_zos_core",
    "github_version": "master",
    "conf_py_path": "/docs/source/",
}

# Currently we are not using these options, for more info follow links:
# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
# https://sphinx-rtd-theme.readthedocs.io/en/stable/
html_theme_options = {
    'prev_next_buttons_location': None,
    #      'canonical_url': '',
    #      'analytics_id': 'UA-XXXXXXX-1',
    #      'logo_only': False,
    #      'display_version': True,
    #      'prev_next_buttons_location': 'bottom',
    #      'style_external_links': False,
    #      'vcs_pageview_mode': '',
    #      'style_nav_header_background': 'white',
    #      # Toc options
    #      'collapse_navigation': True,
    #      'sticky_navigation': True,
    #      'navigation_depth': 4,
    #      'includehidden': True,
    #      'titles_only': False
}


suppress_warnings = [
    'ref.term',  # Suppress WARNING: term not in glossary: 'Managed node' because this is in the parent site.
]
