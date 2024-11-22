# Book Recommendation System

## Create a virtual environment

```
python3 -m venv env
source env/bin/activate
```

## Install the requirements

```
pip install -r requirement.txt
```

## Migrate the database

```
python manage.py migrate
```

## Running the server

```
python manage.py runserver
```

Head to any of the API endpoints given below, say http://127.0.0.1:8000/api/books/

## API Endpoints

### 1. Users:

- POST /api/users/ – Create a new user.
- GET /api/users/ – Retrieve user details.

### 2. Books:

- POST /api/books/ – Add a new book.
- GET /api/books/ – Retrieve all books.

### 3. Preferences

- POST /api/users/preferences/ - Record a preference (like or dislike) for a book.
- DELETE /api/users//preferences/ – Reset a user's preferences.

### 4. Recommendations:

- GET /api/users/recommendations/ – Get book recommendations for a user.
