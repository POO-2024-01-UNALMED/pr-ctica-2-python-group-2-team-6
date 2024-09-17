@echo off
cd /d "%~dp0"

:: Instalar Pillow si no está instalado (solo necesario la primera vez)
pip install Pillow

:: Crear el ejecutable usando pyinstaller. Ajusta la ruta al archivo main.py
pyinstaller --onefile --windowed --add-data "src/uiMain/Imagenes;src/uiMain/Imagenes" src/main.py

:: Ejecutar el script directamente usando la ruta correcta
python src/main.py

:: Pausar para ver posibles errores
pause