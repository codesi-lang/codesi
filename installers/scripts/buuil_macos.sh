#!/bin/bash
echo "Building Codesi for macOS..."

pyinstaller --onefile \
    --name codesi \
    --icon assets/icon.icns \
    --add-data "examples:examples" \
    --windowed \
    codesi/cli.py

echo "Done! Check dist/codesi.app"