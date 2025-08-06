# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'CONAN'
author = 'Ali Raya, Kushal Dey'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/KushalDey02/CONAN",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "collapse_navigation": True,
    "navigation_depth": 4,
}
