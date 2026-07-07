"""Sphinx configuration"""

# -- Imports ------------------------------------------------------------------

from datetime import datetime

# -- Project information ------------------------------------------------------

copyright = f"{datetime.now().year}, René Schwaiger"
project = "DPP Documentation"

# -- General configuration ----------------------------------------------------

extensions = [
    "sphinxcontrib.bibtex",
    "myst_parser",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Bibliography -------------------------------------------------------------

bibtex_bibfiles = ["refs.bib"]
