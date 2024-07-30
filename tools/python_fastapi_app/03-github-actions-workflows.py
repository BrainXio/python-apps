import os
import argparse

def is_app_directory(directory):
    required_files = ["Dockerfile", "pyproject.toml", "app", "tests"]
    return all(os.path.exists(os.path.join(directory, f)) for f in required_files)

def create_github_workflows_for_app(app_name, app_path, workflows_path):
    app_name_with_dashes = app_name.replace('_', '-')
    
    # Define the files with their content
    files = {
        os.path.join(workflows_path, f"{app_name_with_dashes}-test-and-deploy.yml"): f"""
name: Test and Deploy for {app_name}

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install dependencies
      run: |
        cd {app_path}
        poetry install
    - name: Run tests
      run: |
        cd {app_path}
        poetry run pytest

  deploy:
    if: github.ref == 'refs/heads/main'
    needs: test
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install dependencies
      run: |
        cd {app_path}
        poetry install
    - name: Build package
      run: |
        cd {app_path}
        poetry build
    - name: Publish to Test PyPI
      run: |
        cd {app_path}
        python -m pip install twine
        poetry publish --build -r testpypi
      env:
        TWINE_USERNAME: ${{{{ secrets.TEST_PYPI_USERNAME }}}}
        TWINE_PASSWORD: ${{{{ secrets.TEST_PYPI_PASSWORD }}}}

  publish:
    if: github.ref == 'refs/heads/main'
    needs: deploy
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install dependencies
      run: |
        cd {app_path}
        poetry install
    - name: Build package
      run: |
        cd {app_path}
        poetry build
    - name: Publish to PyPI
      run: |
        cd {app_path}
        python -m pip install twine
        poetry publish --build
      env:
        TWINE_USERNAME: ${{{{ secrets.PYPI_USERNAME }}}}
        TWINE_PASSWORD: ${{{{ secrets.PYPI_PASSWORD }}}}
""",
        os.path.join(workflows_path, f"{app_name_with_dashes}-pull-request.yml"): f"""
name: Pull Request Validation for {app_name}

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install dependencies
      run: |
        cd {app_path}
        poetry install
    - name: Run tests
      run: |
        cd {app_path}
        poetry run pytest
""",
        os.path.join(workflows_path, f"{app_name_with_dashes}-release.yml"): f"""
name: Release for {app_name}

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  release:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    - name: Install Poetry
      run: |
        curl -sSL https://install.python-poetry.org | python3 -
        export PATH="$HOME/.local/bin:$PATH"
    - name: Install dependencies
      run: |
        cd {app_path}
        poetry install
    - name: Build package
      run: |
        cd {app_path}
        poetry build
    - name: Generate changelog
      run: |
        gem install github_changelog_generator
        github_changelog_generator -u ${{{{ github.repository_owner }}}} -p ${{{{ github.event.repository.name }}}} -t ${{{{ secrets.GITHUB_TOKEN }}}}
    - name: Commit and push changelog
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
        git add CHANGELOG.md
        git commit -m 'Update CHANGELOG.md'
        git push
    - name: Publish to PyPI
      run: |
        cd {app_path}
        python -m pip install twine
        poetry publish --build
      env:
        TWINE_USERNAME: ${{{{ secrets.PYPI_USERNAME }}}}
        TWINE_PASSWORD: ${{{{ secrets.PYPI_PASSWORD }}}}
    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: {app_path}
        push: true
        tags: ${{{{ secrets.DOCKER_USERNAME }}}}/{app_name_with_dashes}:${{{{ github.ref_name }}}}
        platforms: linux/amd64,linux/arm64
""",
        os.path.join(workflows_path, f"{app_name_with_dashes}-docker-build.yml"): f"""
name: Build and Push Docker Image for {app_name}

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v2
        with:
          platforms: all
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Login to DockerHub
        uses: docker/login-action@v2
        with:
          username: ${{{{ secrets.DOCKER_USERNAME }}}}
          password: ${{{{ secrets.DOCKER_PASSWORD }}}}
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: {app_path}
          push: true
          tags: ${{{{ secrets.DOCKER_USERNAME }}}}/{app_name_with_dashes}:latest
          platforms: linux/amd64,linux/arm64
"""
    }

    # Create files with content
    for filepath, content in files.items():
        with open(filepath, 'w') as file:
            file.write(content)

def create_github_workflows(repo_root):
    workflows_path = os.path.join(repo_root, '.github', 'workflows')
    os.makedirs(workflows_path, exist_ok=True)

    # Detect app directories and create workflows
    for item in os.listdir(repo_root):
        app_path = os.path.join(repo_root, item)
        if os.path.isdir(app_path) and is_app_directory(app_path):
            print(f"Creating workflows for app: {item}")
            create_github_workflows_for_app(item, app_path, workflows_path)

    print("GitHub Actions workflows and Dependabot configuration created successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create GitHub Actions workflows and Dependabot configuration.")
    parser.add_argument('--repo-root', type=str, default='.', help='The root directory of the repository')
    
    args = parser.parse_args()
    create_github_workflows(args.repo_root)
