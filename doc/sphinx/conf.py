"""Sphinx configuration"""

# -- Imports ------------------------------------------------------------------

from datetime import datetime
from pathlib import Path

from sphinx_pyproject import SphinxConfig

# -- Project information ------------------------------------------------------

config = SphinxConfig(
    Path(__file__).parent.parent.parent / "pyproject.toml", globalns=globals()
)
copyright = f"{datetime.now().year}, {author}"  # noqa: F821
project = name  # noqa: F821

# -- General configuration ----------------------------------------------------

extensions = [
    "myst_parser",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
