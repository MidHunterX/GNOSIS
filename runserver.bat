@echo off

echo                                       d8,
echo                                      `8P
echo  d888b8b    88bd88b  d8888b  .d888b,  88b .d888b,
echo d8P' ?88    88P' ?8bd8P' ?88 ?8b,     88P ?8b,
echo 88b  ,88b  d88   88P88b  d88   `?8b  d88    `?8b
echo `?88P'`88bd88'   88b`?8888P'`?888P' d88' `?888P'
echo        i88
echo       ,88P                 for sharing knowledge
echo   `?8888P
echo .
echo .

cd %~dp0
IF EXIST ENV\ (
    call ENV\Scripts\activate.bat
) ELSE (
    echo Virtual environment 'ENV' directory not found.
    echo Using locally installed python instead.
)
start http://localhost:8000
python manage.py runserver
