# Movie Tracker API

A Flask API for keeping a private list of movies you've watched. Users sign
up, log in, and can create, view, update, and delete their own movie
entries. Nobody can see or touch another user's list.

## Tech

- Flask + Flask-RESTful
- Flask-SQLAlchemy + Flask-Migrate
- Flask-bcrypt (password hashing)
- Session-based auth
- Marshmallow (request validation)
- SQLite3 (dev database)

## Installation

```bash
pipenv install && pipenv shell
```

## Create a `.env` file in the project root containing the following:

SECRET_KEY=your-secret-key
DATABASE_URI=sqlite:///app.db

## Set up the database:

```bash
cd server
export FLASK_APP=app.py
flask db upgrade
python seed.py
```

## Running

```bash
cd server
python app.py
```

The API runs at `http://127.0.0.1:5555`.

## Endpoints

| Method | Route             | Auth required  | Description                                |
|--------|-------------------|----------------|--------------------------------------------|
| POST   | `/signup`         | No             | Create an account, logs the user in        |
| POST   | `/login`          | No             | Log in with username/password              |
| DELETE | `/logout`         | No             | Clear the current session                  |
| GET    | `/check_session`  | No             | Return the current logged-in user          |
| GET    | `/movies`         | Yes            | List the current user's movies (paginated) |
| POST   | `/movies`         | Yes            | Create a movie                             |
| PATCH  | `/movies/<id>`    | Yes            | Update a movie you've seen                 |
| DELETE | `/movies/<id>`    | Yes            | Delete a movie you've seen                 |

`GET /movies` accepts `?page=` and `?per_page=` query params (defaults:
page 1, 10 per page).
