> Self Note: Revoke Gemini API Key after presentation

![](./assets/header.png)

> For sharing knowledge

The "GNOSIS-for sharing knowledge" is an ambitious project designed to transform the way individuals engage with and acquire knowledge in the realm of computer functionality. In today's rapidly evolving technological landscape, the demand for comprehensive and accessible information has never been greater. This platform seeks to bridge the gap between complex technical concepts and userfriendly learning by providing a dynamic and interactive space where users can post questions and receive tailored responses in their preferred format. At its core, the platform is built on the foundation of inclusivity and accessibility, recognizing that users have diverse learning styles and preferences.

# 💻 Development Progress

- ![](https://geps.dev/progress/100) Concept of operation
- ![](https://geps.dev/progress/100) Requirements elicitation
- ![](https://geps.dev/progress/100) Database Modelling and Implementation
- ![](https://geps.dev/progress/100) Backend Server Logic Design and Implementation
- ![](https://geps.dev/progress/85) UI/UX Design and Implementation
- ![](https://geps.dev/progress/0) Blackbox Testing

# ⚙️ Project Features

## Profile Related Features

- [x] Register an account
- [x] Show error messages on unsuccessful authentication
- [x] Login with registered account on successful authentication
- [x] Edit registered account details
- [x] Upload Pictures to set as Profile Display Picture in account settings
- [x] Logout of registered account
- [x] View own registered account
- [x] View other registered accounts
- [x] Upload Pictures for Profile Picture
- [x] Toggle between Uploader and Viewer Mode

## Question Related Features

- [x] Create questions in plaintext
- [x] Read questions
- [x] Update questions in plaintext
- [x] Delete questions
- [x] Add questions to favorites list
- [x] Optional ability to restrict comments on study materials / posts
- [x] Auto Generate answers with Gemini AI
- [x] Answer questions asked by other registered accounts in plaintext
- [x] Answer questions asked by other registered accounts in markdown
  - [x] Sanitize problematic HTML tags for security
  - [x] Model in Database for storing Sanitized Data
  - [x] Renderer for stored markdown code
- [x] Answer questions asked by other registered accounts with inline image (url) attachment
- [x] Answer questions asked by other registered accounts in audio
- [x] Answer questions asked by other registered accounts in video

## User Interface Features

- [x] Switch between Light mode and Dark mode
- [x] Fully featured markdown input formatting UI
- [x] Query questions using fuzzy logic
- [x] Generative AI Answer and Fuzzy Search questions logic using a single search bar
- [x] Show Generating Status on Answer Generation
- [x] Split Uploader/Viewer mode selection screen
- [x] Dropdown list for all Profile Functions

## Optional Features
- [x] Show a welcome page after login
- [x] Show a goodbye page after logout
- [x] On goodbye page, redirect users to login page after n seconds
- [x] Human readable approximate timestamps
- [ ] Set default engineering department in account settings
- [ ] Generate research materials with duckduckgo API
- [ ] Search for questions and answers based on Department
- [ ] Explore questions based on Department
- [ ] Answer Code Syntax Highlighting with Pygments

# 📦 Technologies Used

| Name                 | Usage                                       |
| -------------------- | ------------------------------------------- |
| virtualenv           | Python package virtual environment          |
| Django               | Python webapp framework                     |
| django-crispy-forms  | For all Input Forms                         |
| crispy-bootstrap5    | Bootstrap for Crispy Forms                  |
| django-markdownfield | Raw Markdown storage model and renderer     |
| bleach               | HTML Sanitizier for storing MD to DB        |
| Bootstrap v5.3       | CSS Framework                               |
| Fontawesome          | CSS Icons Framework                         |
| easymde              | Markdown Editor Frontend for User Input     |
| fuzzywuzzy           | Fuzzy String Sequence and Pattern detection |
| python-Levenshtein   | String similarity and distance operations   |

# 🆕 Initializing Project

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

# 🏃 Running Project

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

# ⚠️ Problems Faced

### Question Search Logic

Task: Search for an input question in a database. If question found, return question; else, return generated answer.

- Searching for questions based on string comparison won't work on spelling mistakes and rephrased questions
- Spelling mistakes issue can be solved using Levenshtein distance which finds the similarity of two strings
- With that set, the rest of the input can be compared using Fuzzy Logic which returns questions similar enough
- So, the best approach is to use Fuzzy Logic based on string similarity percentage.
- If similarity percentage is set high, it might skip slightly rephrased questions.
- If similarity percentage is set low, wrong questions with similar words might be returned.

# ✂️ Snippets for Development

### Re-applying Migrations (Col not found error)

```sh
python manage.py migrate gnosis_app zero
python manage.py migrate
```
