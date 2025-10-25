#!/bin/bash
echo "Building Codesi for Linux..."

pyinstaller --onefile \
    --name codesi \
    --icon assets/icon.ico \
    --add-data "examples:examples" \
    --console \
    codesi/cli.py

echo "Done! Check dist/codesi"