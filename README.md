# Django forms and templates

A Django project with 1 model, a REST API (Django REST Framework) and HTML templates.

## Tech stack

- Python 3
- Django
- Pillow
- requests
- Django REST Framework
- Database: SQLite

## Project structure

- `django_forms_and_templates/`: project settings and root URLs
- `player_app/`: Django app
- `theme/`: Django app
- 4 HTML templates
- Tests: `player_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Player` | `player_app` | name, birthDate, country, email, tshirtNumber, photo, password, gender, description, hobbies |

## URL routes

Declared in `urls.py`:

- `/blog/`
- `/players/`
- `/__reload__/`
- `/add-player/`
- `/list/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
