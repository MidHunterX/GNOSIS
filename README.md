# GNOSIS

## Project Structure

Python ENV - ./ENV/
Django App - ./GNOSIS/

## Initializing Project

### Initialize Virtual Environment

Remove ENV directory if it already exists then recreate virtual environment:

```sh
install python
python -m pip install virtualenv
python -m venv ENV
```

### Activate Virtual Environment

```sh
./ENV/Scripts/activate.bat
pip install django
pip install -r requirements.txt
```

### Create Admin Account

```sh
python manage.py createsuperuser
```
```
Username: admin
Email address: admin@gnosis.com
Password: admin
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
and open: 127.0.0.1:8000

## Closing Project

```
deactivate
```

## Snippets for Development

### Migrate model after changes

```sh
python manage.py makemigrations
python manage.py migrate
```

### Re-applying Migrations (Col not found error)

```sh
python manage.py migrate gnosis_app zero
python manage.py migrate
```
