#!/bin/bash

# Exit on error
set -e

# Clean up old builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Upload to PyPI
python -m twine upload dist/*

echo "Package uploaded successfully!" 