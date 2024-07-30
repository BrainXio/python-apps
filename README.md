# PythonAppGenerator-Template

A template repository for generating various Python applications with integrated CLI capabilities, Docker support, and comprehensive testing setups. Ideal for quickly starting new Python projects with robust and scalable structures.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
    - [Step 1: Generate the App Base](#step-1-generate-the-app-base)
    - [Step 2: Commit the App Base](#step-2-commit-the-app-base)
    - [Step 3: Generate GitHub Actions Workflows](#step-3-generate-github-actions-workflows)
    - [Step 4: Commit GitHub Actions Workflows](#step-4-commit-github-actions-workflows)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the PythonAppGenerator-Template repository. This repository provides tools to generate a well-structured Python application with FastAPI integration, CLI capabilities, Docker support, and a comprehensive testing setup. This template is perfect for quickly starting new Python projects with robust and scalable structures.

## Prerequisites

Before using the tools provided in this repository, ensure you have the following installed on your system:

- Python 3.7 or higher
- Poetry (for dependency management)
- Docker (optional, for containerization)
- Git (for version control)

## Getting Started

Follow these steps to generate and set up your Python application:

### Step 1: Generate the App Base

1. Start from the root of the directory directory:

2. Run the `01-generate-app-base.py` script to create the project structure:

    ```sh
    python tools/python_fastapi_app/01-generate-app-base.py
    ```

    By default, this script will generate a FastAPI application with the following parameters:
    - `name`: `example_app`
    - `version`: `0.1.0`
    - `description`: `A FastAPI application with Pydantic models and CLI capabilities.`
    - `authors`: `["Your Name <your.email@example.com>"]`

3. You can customize the project parameters by providing optional arguments:

    ```sh
    python tools/python_fastapi_app/01-generate-app-base.py --name example_app --version 1.0.0 --description "A custom FastAPI app" --authors "Jane Doe <jane.doe@example.com>"
    ```

### Step 2: Commit the App Base

1. Run the `02-commit-app-base.py` script to commit and push the generated project files to a new git branch:

    ```sh
    python tools/python_fastapi_app/02-commit-app-base.py
    ```

    By default, this script will commit the files to a branch named `feature/initial-setup` for the project named `example_app`.

2. You can customize the project name by providing an optional argument:

    ```sh
    python tools/python_fastapi_app/02-commit-app-base.py --name example_app
    ```

### Step 3: Generate GitHub Actions Workflows

1. Run the `03-github-actions-workflows.py` script to generate the GitHub Actions workflows for all detected apps:

    ```sh
    python tools/python_fastapi_app/03-github-actions-workflows.py --repo-root .
    ```

### Step 4: Commit GitHub Actions Workflows

1. Run the `04-commit-github-actions-workflows.py` script to commit and push the GitHub Actions workflows to a new git branch:

    ```sh
    python tools/python_fastapi_app/04-commit-github-actions-workflows.py
    ```

## Project Structure

After generating the project, you will see a directory structure similar to the following:

```
example_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── __init__.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── dependencies/
│   │   ├── __init__.py
│   │   └── auth.py
│   └── schemas/
│       ├── __init__.py
│       └── user.py
├── cli/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_user.py
├── .env
├── .dockerignore
├── Dockerfile
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

### Installing Dependencies

Navigate to your project directory and install the dependencies using Poetry:

```sh
cd example_app
poetry install
```

Alternatively, use pip to install the dependencies:

```sh
pip install -r requirements.txt
```

### Running the Application

To start the FastAPI application, run:

```sh
uvicorn app.main:app --reload
```

### Running Tests

To run the tests, use:

```sh
pytest
```

### Building and Running the Docker Container

To build the Docker image, use the Makefile:

```sh
make build-image
```

To run the Docker container:

```sh
make run-container
```

### Using the CLI

The script includes a basic CLI tool. To use it, run:

```sh
python -m example_app.cli.main hello
```

This will print "Hello from CLI!".

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the Unlicense License - see the [LICENSE](LICENSE) file for details.
