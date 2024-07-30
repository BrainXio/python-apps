import os
import subprocess
import argparse

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def create_branch(branch_name):
    run_command(f"git checkout -b {branch_name}")

def add_file(filepath):
    run_command(f"git add {filepath}")

def commit_file(filepath, message):
    run_command(f'git commit -m "{message}" {filepath}')

def push_branch(branch_name):
    run_command(f"git push -u origin {branch_name}")

def main(name):
    name_with_dashes = name.replace('_', '-')

    commit_messages = {
        f"{name}/app/__init__.py": "Add init file for app module",
        f"{name}/app/main.py": "Add main FastAPI application entry point",
        f"{name}/app/models/__init__.py": "Add init file for models module",
        f"{name}/app/routers/__init__.py": "Add init file for routers module",
        f"{name}/app/routers/user.py": "Add user routes",
        f"{name}/app/dependencies/__init__.py": "Add init file for dependencies module",
        f"{name}/app/dependencies/auth.py": "Add basic authentication dependency",
        f"{name}/app/schemas/__init__.py": "Add init file for schemas module",
        f"{name}/app/schemas/user.py": "Add user Pydantic models",
        f"{name}/tests/__init__.py": "Add init file for tests module",
        f"{name}/tests/test_main.py": "Add tests for main application",
        f"{name}/tests/test_user.py": "Add tests for user routes",
        f"{name}/cli/__init__.py": "Add init file for CLI module",
        f"{name}/cli/main.py": "Add basic CLI implementation",
        f"{name}/.env": "Add environment variables file",
        f"{name}/.dockerignore": "Add .dockerignore file",
        f"{name}/__init__.py": "Add init file for main module",
        f"{name}/Dockerfile": "Add Dockerfile for containerization",
        f"{name}/pyproject.toml": "Add pyproject.toml for project configuration",
        f"{name}/requirements.txt": "Add requirements.txt for dependencies",
        f"{name}/README.md": "Add README.md with project details",
        f"{name}/Makefile": "Add Makefile for project automation",
    }
    
    branch_name = f"feature/{name_with_dashes}"
    create_branch(branch_name)
    
    for filepath, message in commit_messages.items():
        if os.path.exists(filepath):
            add_file(filepath)
            commit_file(filepath, message)
    
    push_branch(branch_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Commit and push project files to a new git branch.")
    parser.add_argument('--name', type=str, default='example_app', help='The name of the FastAPI application')
    
    args = parser.parse_args()
    main(args.name)
