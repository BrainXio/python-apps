import os
import argparse

def create_project_structure(name, version, description, authors):
    name_with_dashes = name.replace('_', '-')
    
    # Define the directory structure
    directories = [
        name,
        f"{name}/app",
        f"{name}/app/models",
        f"{name}/app/routers",
        f"{name}/app/dependencies",
        f"{name}/app/schemas",
        f"{name}/tests",
        f"{name}/cli"
    ]

    # Define the files with their content
    files = {
        f"{name}/__init__.py": "",
        f"{name}/app/__init__.py": "",
        f"{name}/app/main.py": f"""
from fastapi import FastAPI
from app.routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {{"message": "Welcome to the FastAPI application!"}}
""",
        f"{name}/app/models/__init__.py": "",
        f"{name}/app/routers/__init__.py": "",
        f"{name}/app/routers/user.py": f"""
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users_db = []

@router.post("/", response_model=User)
def create_user(user: UserCreate):
    new_user = User(id=len(fake_users_db) + 1, **user.dict())
    fake_users_db.append(new_user)
    return new_user

    
@router.get("/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10):
    return fake_users_db[skip: skip + limit]
""",
        f"{name}/app/dependencies/__init__.py": "",
        f"{name}/app/dependencies/auth.py": """
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "secret-api-key"
api_key_header = APIKeyHeader(name="api_key")

def get_current_user(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"username": "testuser"}
""",
        f"{name}/app/schemas/__init__.py": "",
        f"{name}/app/schemas/user.py": """
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
""",
        f"{name}/tests/__init__.py": "",
        f"{name}/tests/test_main.py": f"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {{"message": "Welcome to the FastAPI application!"}}
""",
        f"{name}/tests/test_user.py": f"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={{"username": "john", "email": "john@example.com", "password": "secret"}})
    assert response.status_code == 200
    assert response.json()["username"] == "john"
    assert "password" not in response.json()

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
""",
        f"{name}/cli/__init__.py": "",
        f"{name}/cli/main.py": """
import click

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo("Hello from CLI!")

cli.add_command(hello)

if __name__ == "__main__":
    cli()
""",
        f"{name}/.env": "API_KEY=secret-api-key\n",
        f"{name}/.dockerignore": """
__pycache__
*.pyc
.env
venv/
*.egg-info
build/
dist/
.coverage
.cache
pytest_cache/
htmlcov/
.tox/
.mypy_cache/
.ipynb_checkpoints
poetry.lock
cython_debug/
""",
        f"{name}/Dockerfile": f"""
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
        f"{name}/pyproject.toml": f"""
[tool.poetry]
name = "{name}"
version = "{version}"
description = "{description}"
authors = {authors}

packages = [
    {{ include = "app" }},
    {{ include = "cli" }}
]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.70.1"
uvicorn = "^0.15.0"
pydantic = "^1.8.2"
click = "^8.0.1"
requests = "^2.26.0"

[tool.poetry.dev-dependencies]
pytest = "^6.2.5"

[tool.poetry.scripts]
{name_with_dashes} = "cli.main:cli"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
""",
        f"{name}/requirements.txt": """
fastapi==0.70.1
uvicorn==0.15.0
pydantic==1.8.2
click==8.0.1
pytest==6.2.5
requests=="2.26.0"
""",
        f"{name}/README.md": f"""
# {name.replace('_', ' ').title()}

{description}
""",
        f"{name}/Makefile": f"""
.PHONY: install poetry-install pip-install run test lint format build-image run-container

install: poetry-install pip-install

poetry-install:
\tpoetry install

pip-install:
\tpip install .

run:
\tuvicorn app.main:app --reload

test:
\tpytest

lint:
\tflake8 .

format:
\tblack .

build-image:
\tdocker build -t {name_with_dashes} .

run-container:
\tdocker run -d -p 8000:8000 --env-file .env {name_with_dashes}
"""
    }

    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create files with content
    for filepath, content in files.items():
        with open(filepath, 'w') as file:
            file.write(content)

    print("Project structure created successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a FastAPI project structure.")
    parser.add_argument('--name', type=str, default='example_app', help='The name of the FastAPI application')
    parser.add_argument('--version', type=str, default='0.1.0', help='The version of the FastAPI application')
    parser.add_argument('--description', type=str, default='A FastAPI application with Pydantic models and CLI capabilities.', help='The description of the FastAPI application')
    parser.add_argument('--authors', type=list, default=["Your Name <your.email@example.com>"], help='The authors of the FastAPI application')

    args = parser.parse_args()
    create_project_structure(args.name, args.version, args.description, args.authors)
