# JWT_AuthSystem (FastAPI + SQLAlchemy)

A minimal FastAPI example using SQLAlchemy and PostgreSQL to manage a simple users table. The code in main.py provides endpoints to create and fetch users.

## Features
- FastAPI web app
- SQLAlchemy ORM models
- PostgreSQL (psycopg driver)
- Pydantic models for request/response (pydantic v2 style)

## Requirements
- Python 3.10+
- PostgreSQL server

Recommended Python packages (install with pip):
```
fastapi
uvicorn
sqlalchemy>=2.0
pydantic>=2.0
psycopg[binary]
```

## Setup
1. Clone repository and cd into project root.
2. Create a PostgreSQL database and user. Example:
   - createdb learn
   - createuser -P nanashi
   - grant privileges as needed
3. Set environment variable (recommended) or edit DATABASE_URL in main.py:

```bash
export DATABASE_URL="postgresql+psycopg://<user>:<password>@localhost:5432/<database>"
```

(Example from main.py: postgresql+psycopg://nanashi:Nanashi0210@localhost:5432/learn)

## Run the app
Install dependencies and start the server:

```bash
pip install -r requirements.txt   # or pip install fastapi uvicorn sqlalchemy pydantic psycopg[binary]
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open http://127.0.0.1:8000/docs for interactive API docs (Swagger UI).

## API Endpoints
- GET /
  - Returns a welcome message.
  - Example: curl http://127.0.0.1:8000/

- GET /users/{user_id}
  - Response model: UserResponse
  - Example: curl http://127.0.0.1:8000/users/1

- POST /users/
  - Create a new user. Request body (JSON):
    ```json
    {
      "name": "Alice",
      "email": "alice@example.com",
      "roll": "42"
    }
    ```
  - Example: curl -X POST "http://127.0.0.1:8000/users/" -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com","roll":"42"}'

## Notes & Suggestions
- main.py currently hardcodes DATABASE_URL; prefer using environment variables for security.
- The code uses Pydantic v2's `from_attributes = True` for response models (equivalent to `orm_mode` in v1).
- A stray call to `get_db()` exists at module import (line that invokes the generator). Remove it — it opens a DB session on import.
- Consider using Alembic for schema migrations and adding password hashing and authentication if expanding to a full auth system.

## License
Use as desired. No license file included.
