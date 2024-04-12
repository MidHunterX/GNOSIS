cd %~dp0
IF EXIST ENV\ (
    call ENV\Scripts\activate.bat
) ELSE (
    echo Virtual environment 'ENV' directory not found.
    echo Using locally installed python instead.
)
echo Updating Codebase from Git Remote Server...
git pull
echo Checking for python dependency updates...
pip install -r requirements.txt
