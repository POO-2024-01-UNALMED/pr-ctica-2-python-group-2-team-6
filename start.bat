@echo off
cd /d "%~dp0"

:: Instalar Pillow si no está instalado (solo necesario la primera vez)
pip install Pillow

:: Ejecutar el script directamente usando la ruta correcta
python src/main.py

:: Pausar para ver posibles errores
pause