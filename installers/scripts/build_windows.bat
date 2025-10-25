@echo off
echo Building Codesi for Windows...

pyinstaller --onefile ^
    --name codesi ^
    --icon assets/icon.ico ^
    --add-data "examples;examples" ^
    --console ^
    ../../codesi/cli.py

echo Done! Check dist/codesi.exe
pause