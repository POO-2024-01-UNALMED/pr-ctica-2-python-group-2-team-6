@echo off
cd /d "%~dp0"

:: Instalar Pillow si no está instalado (esto solo es necesario la primera vez)
pip install Pillow

:: Crear el ejecutable usando pyinstaller
pyinstaller --onefile --windowed --add-data "src/uiMain/Imagenes;src/uiMain/Imagenes" src/main.py

:: Pausar para ver posibles errores
pause
