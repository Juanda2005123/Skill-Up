@echo off
REM Script para manejar operaciones de Django
echo Entrando al entorno de Django...

REM Verifica y elimina la base de datos (personaliza según el motor de BD)
IF EXIST db.sqlite3 (
    echo Borrando base de datos...
    del db.sqlite3
)

REM Ejecutar makemigrations y migrate
echo Creando migraciones y aplicándolas...
python manage.py makemigrations
python manage.py migrate

echo Django listo.
pause
