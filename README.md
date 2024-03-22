# GNOSIS

## Project Structure

| Directory     | Description         |
| ------------- | ------------------- |
| ./GNOSIS/     | Main Django Project |
| ./gnosis_app/ | GNOSIS Webapp       |
| ./media/      | Multimedia storage  |
| ./static/     | Static Dependencies |

## Technologies Used

| Name                | Usage                              |
| ------------------- | ---------------------------------- |
| virtualenv          | Python package virtual environment |
| Django              | Python webapp framework            |
| django-crispy-forms | For all Input Forms                |
| crispy-bootstrap5   | Bootstrap for Crispy Forms         |


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

recreate database migrations

```sh
python manage.py migrate gnosis_app zero
python manage.py migrate
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
