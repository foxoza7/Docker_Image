@echo off
# Esta línea mueve el terminal a la carpeta donde está este archivo .bat
cd /d "%~dp0"

echo Iniciando servidor X...
REM Cambia la ruta a donde guardaste tu archivo .xlaunch
start "" "%~dp0MiCalculadora.xlaunch"
echo Esperando 5 segundos a que XServer arranque...
timeout /t 5

echo Esperando 5 segundos...
timeout /t 5

echo Lanzando contenedor con Docker Compose...
docker-compose up --build

pause