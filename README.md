# GNOSIS

## Requirements

- Python
- python -m pip install virtualenv
- python -m pip install django

## Project Structure

Python ENV - ./ENV/
Django App - ./GNOSIS/

## Starting Fresh

Remove ENV directory if it already exists then recreate virtual environment:

```sh
python -m venv ENV
./ENV/Scripts/activate.bat
pip install django
pip install -r requirements.txt
```

## Running Project

cd into this project and Activate virtual environment:

```sh
# Powershell
.\ENV\Scripts\Activate.ps1
# CMD
.\ENV\Scripts\activate.bat
# Bash and Zsh
source ENV/bin/activate
# Fish
source ENV/bin/activate.fish
```

Run server:

```
python manage.py runserver
```

## Refresh

```sh
python manage.py makemigrations
python manage.py migrate
```

## Closing Project

```
deactivate
```
