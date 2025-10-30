# FastAPI Supabase App

This project is a FastAPI application that utilizes Supabase PostgreSQL as the database. It includes features such as user authentication, database migrations with Alembic, and a seeder for initial data population.

## Project Structure

```
fastapi-supabase-app
├── src
│   ├── main.py
│   ├── app
│   │   ├── api
│   │   │   └── v1
│   │   │       ├── endpoints
│   │   │       │   ├── auth.py  # Authentication-related endpoints
│   │   │       │   ├── users.py  # User-related endpoints
│   │   │       │   └── items.py  # Item-related endpoints
│   │   │       └── __init__.py   # Initializes API version 1 module
│   │   ├── auth
│   │   │   ├── jwt.py           # JWT creation and verification
│   │   │   ├── service.py       # Authentication services
│   │   │   └── deps.py          # Dependency functions for authentication
│   │   ├── core
│   │   │   ├── config.py        # Configuration settings
│   │   │   └── security.py      # Security-related functions
│   │   ├── db
│   │   │   ├── session.py       # Database session management
│   │   │   ├── base.py          # Base model for SQLAlchemy
│   │   │   └── supabase_client.py # Supabase PostgreSQL client setup
│   │   ├── models
│   │   │   ├── __init__.py      # Initializes models module
│   │   │   └── user.py          # User model definition
│   │   ├── crud
│   │   │   └── user.py          # CRUD operations for User model
│   │   ├── schemas
│   │   │   └── user.py          # Pydantic schemas for user data
│   │   ├── middlewares
│   │   │   └── auth_middleware.py # Authentication middleware
│   │   ├── seeds
│   │   │   └── seed_users.py    # Logic for seeding database with users
│   │   └── deps.py              # Application-wide dependencies
│   └── tests
│       ├── conftest.py          # Configuration for pytest
│       └── test_users.py        # Tests for user functionalities
├── alembic.ini                  # Alembic configuration file
├── alembic
│   ├── env.py                   # Alembic environment script
│   └── versions
│       └── 0001_create_users_table.py # Migration script for users table
├── requirements.txt             # Project dependencies
├── pyproject.toml               # Project configuration file
├── .env.example                 # Example environment variables
├── Dockerfile                   # Docker image build instructions
├── docker-compose.yml           # Docker Compose configurations
└── README.md                    # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-supabase-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and fill in the required values.

5. **Run database migrations:**
   ```
   alembic upgrade head
   ```

6. **Seed the database:**
   ```
   python -m src.app.seeds.seed_users
   ```

7. **Start the FastAPI application:**
   ```
   uvicorn src.main:app --reload
   ```

## Usage

- Access the API documentation at `http://localhost:8000/docs`.
- Use the authentication endpoints to register and log in users.
- Manage users and items through the respective endpoints.

## License

This project is licensed under the MIT License.