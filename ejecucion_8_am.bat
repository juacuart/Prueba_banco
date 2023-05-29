@echo off

REM Activar el entorno virtual
echo Activando el entorno virtual...
call C:\Users\juacuart\Documents\Material_de_trabajo\Prueba\Prueba_banco\venv\Scripts\activate.bat

REM Ejecutar el primer script de Python
echo Ejecutando ejecucion_8_am.py...
python C:\Users\juacuart\Documents\Material_de_trabajo\Prueba\Prueba_banco\python\ejecucion_8_am.py

REM Desactivar el entorno virtual
echo Desactivando el entorno virtual...
deactivate

