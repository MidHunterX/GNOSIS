# GNOSIS

> For sharing knowledge

## Development Progress

- [x] Concept of operation
- [x] Requirements elicitation
- [x] Database Modelling
- [ ] Logic Design and Implementation
- [ ] UI/UX Design and Implementation
- [ ] Blackbox Testing

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
- [x] Auto Generate answers with LLMs
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

| Name                 | Usage                              |
| -------------------- | ---------------------------------- |
| virtualenv           | Python package virtual environment |
| Django               | Python webapp framework            |
| django-crispy-forms  | For all Input Forms                |
| crispy-bootstrap5    | Bootstrap for Crispy Forms         |
| django-markdownfield | Markdown input and storage         |
| Bootstrap v5.3       | CSS Framework                      |
| Fontawesome          | CSS Icons Framework                |

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
# Powershell
.\ENV\Scripts\Activate.ps1
# CMD
.\ENV\Scripts\activate.bat
# Bash and Zsh
source ENV/bin/activate
# Fish
source ENV/bin/activate.fish
```

### Install Requirements

```sh
pip install -r requirements.txt
```

### Create Admin Account

```sh
python manage.py createsuperuser
```

Username: admin
Email address: admin@gnosis.com
Password: admin

## Running Project

cd into this project and do the following steps

### Activate Virtual Environment

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

### Run Server

```
python manage.py runserver
```

Open 127.0.0.1:8000 in your browser

### Closing Virtual Environment

Press Ctrl+C to close the server and 
either close the server console window or use the following command

```
deactivate
```

# UI/UX Design Inspirations

These are design choices made by big tech companies which are proven to be one of the best designs when it comes to rich user experience.

| Style Inspiration               | Project Implementation                         |
| ------------------------------- | ---------------------------------------------- |
| NFS Rivals style selection mode | Full screen modal. Esc to quit bottom tagline. |
| Whatsapp Group style Message    | Answer suggestions                             |
| Quora style answers             | ques_details page                              |
| Gmail Textbox style MD input    | ques_details page multimedia input             |
| Whatsapp Attach UI              | ques_details input more section                |

## Snippets for Development

### Re-applying Migrations (Col not found error)

```sh
python manage.py migrate gnosis_app zero
python manage.py migrate
```
