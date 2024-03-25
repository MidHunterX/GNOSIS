# GNOSIS

> For sharing knowledge

## Development Progress

- ![](https://geps.dev/progress/100) Concept of operation
- ![](https://geps.dev/progress/100) Requirements elicitation
- ![](https://geps.dev/progress/90) Database Modelling and Implementation
- ![](https://geps.dev/progress/50) Program Logic Design and Implementation
- ![](https://geps.dev/progress/10) UI/UX Design and Implementation
- ![](https://geps.dev/progress/0) Blackbox Testing

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
- [x] Auto Generate answers with Gemini AI
- [x] Answer questions asked by other registered accounts in plaintext
- [ ] Answer questions asked by other registered accounts in markdown
- [ ] Answer questions asked by other registered accounts in audio
- [ ] Answer questions asked by other registered accounts in video
- [ ] Search for all questions and answers
- [ ] Search for questions and answers based on Department
- [ ] Explore questions based on Department
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

### Clone the project

```sh
git clone https://github.com/MidHunterX/GNOSIS
```

### Initialize Virtual Environment

Install Python and execute following commands:

```sh
python -m pip install virtualenv
python -m venv ENV
```

### Activate Virtual Environment

Powershell

```sh
.\ENV\Scripts\Activate.ps1
```

CMD

```sh
.\ENV\Scripts\activate.bat
```

Bash and Zsh

```sh
source ENV/bin/activate
```

Fish

```sh
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

Username: admin <br>
Email address: admin@gnosis.com <br>
Password: admin

## Running Project

cd into this project and do the following steps

### Activate Virtual Environment

Powershell

```sh
.\ENV\Scripts\Activate.ps1
```

CMD

```sh
.\ENV\Scripts\activate.bat
```

Bash and Zsh

```sh
source ENV/bin/activate
```

Fish

```sh
source ENV/bin/activate.fish
```

### Run Server

```sh
python manage.py runserver
```

Open 127.0.0.1:8000 in your browser

### Closing Virtual Environment

Press Ctrl+C to close the server and either close the server console window or use the following command

```
deactivate
```

## UI/UX Design Inspirations

These are design choices made by big tech companies which are proven to be one of the best designs when it comes to rich user experience.

| Style Inspiration            | Project Implementation                         |
| ---------------------------- | ---------------------------------------------- |
| Rivals style selection mode  | Full screen modal. Esc to quit bottom tagline. |
| Whatsapp Group style Message | Answer suggestions                             |
| Quora style answers          | ques_details page                              |
| Gmail Textbox style MD input | ques_details page multimedia input             |
| Whatsapp Attach UI           | ques_details input more section                |

## Snippets for Development

### Re-applying Migrations (Col not found error)

```sh
python manage.py migrate gnosis_app zero
python manage.py migrate
```
