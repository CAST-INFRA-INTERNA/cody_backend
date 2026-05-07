#!/bin/bash

# Cody Backend - Documentation deployment script

set -e

echo "Cody Backend - Documentation deployment script"
echo "================================="

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "UV is not installed, installing now..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed, please install Git first"
    exit 1
fi

# Install documentation dependencies
echo "Installing documentation dependencies..."
uv sync --group docs

# Build documentation
echo "Building documentation..."
uv run mkdocs build

# Check build result
if [ -d "site" ]; then
    echo "Documentation built successfully!"
    echo "Build files located at: site/"
else
    echo "Documentation build failed"
    exit 1
fi

# Show local preview info
echo ""
echo "Local preview:"
echo "   uv run mkdocs serve"
echo "   Access URL: http://localhost:8000"
echo ""
echo "Documentation system setup complete!"
