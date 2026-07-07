# -- Settings ------------------------------------------------------------------

# Use latest version of PowerShell on Windows
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]

# -- Variables -----------------------------------------------------------------

package := "icotest"

sphinx_input := "doc/sphinx"
sphinx_output := "build/sphinx"

# -- Recipes -------------------------------------------------------------------

# Setup Python environment
[group('setup')]
[private]
setup:
	uv venv --allow-existing
	uv pip install -r requirements.txt

# Generate documentation
[group('documentation')]
[default]
documentation: setup
	uv run sphinx-build -M html {{sphinx_input}} {{sphinx_output}}

# Remove documentation
[group('documentation')]
[windows]
clean:
	#!pwsh
	Remove-Item -Recurse {{sphinx_output}}

# Remove documentation
[group('documentation')]
[unix]
clean:
	#!/usr/bin/env sh -e
	rm -rf {{sphinx_output}}
