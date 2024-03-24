# GNOSIS

> For sharing knowledge

## Project Requirements

### Profile Related Requirements

- [x] Register an account
- [x] Show error messages on unsuccessful authentication
- [x] Login with registered account on successful authentication
- [x] Edit registered account details
- [x] Logout of registered account
- [x] View other registered accounts

### General Requirements

- [x] Upload Pictures for Profile Picture
- [x] Switch between Light mode and Dark mode

### Question Related Requirements

- [x] Create questions in plaintext
- [x] Read questions
- [x] Update questions in plaintext
- [x] Delete questions
- [x] Add questions to favorites list
- [x] Optional ability to restrict comments on study materials / posts
- [x] Toggle between Uploader and Viewer Mode
- [x] Answer questions asked by other registered accounts in plaintext
- [ ] Answer questions asked by other registered accounts in markdown
- [ ] Answer questions asked by other registered accounts in audio
- [ ] Answer questions asked by other registered accounts in video
- [ ] Search for all questions and answers
- [ ] Search for questions and answers based on Department
- [ ] Explore questions based on Department
- [ ] Generate answers using OpenAI API
- [ ] Generate research materials with duckduckgo API

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
