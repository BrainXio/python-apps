# Contributing to PythonAppGenerator-Template

Thank you for considering contributing to the PythonAppGenerator-Template project! Your contributions help improve the quality and functionality of this repository. Whether you're reporting bugs, suggesting features, or submitting pull requests, your efforts are greatly appreciated.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Features](#suggesting-features)
    - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Workflow](#development-workflow)
- [Style Guide](#style-guide)
- [License](#license)

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How to Contribute

### Reporting Bugs

If you encounter a bug or unexpected behavior, please help us by reporting it. Use the GitHub [Issues](https://github.com/brainxio/pythonappgenerator-template/issues) section and include the following information:

- A clear and descriptive title.
- A detailed description of the issue.
- Steps to reproduce the issue.
- Any relevant logs, screenshots, or code snippets.

### Suggesting Features

We welcome suggestions for new features and enhancements. To propose a new feature, create a new issue in the GitHub [Issues](https://github.com/brainxio/pythonappgenerator-template/issues) section and include the following details:

- A clear and descriptive title.
- A detailed description of the proposed feature.
- Any relevant use cases or examples.

### Submitting Pull Requests

If you'd like to contribute code, follow these steps:

1. Fork the repository to your GitHub account.
2. Clone your fork to your local machine:

    ```sh
    git clone https://github.com/brainxio/pythonappgenerator-template.git
    ```

3. Create a new branch for your feature or bugfix:

    ```sh
    git checkout -b feature/your-feature-name
    ```

4. Make your changes, ensuring you follow the project's coding standards and commit message conventions.
5. Push your changes to your fork:

    ```sh
    git push origin feature/your-feature-name
    ```

6. Open a pull request on the original repository. Provide a clear and descriptive title and description of your changes.

## Development Workflow

1. Ensure all dependencies are installed:

    ```sh
    poetry install
    ```

2. Run tests to verify your changes:

    ```sh
    pytest
    ```

3. Lint your code to ensure it follows the style guide:

    ```sh
    flake8 .
    ```

4. Format your code for consistency:

    ```sh
    black .
    ```

5. Update the documentation if your changes affect usage or features.

## Style Guide

- **Python Code**: Follow PEP 8 guidelines. Use `flake8` for linting and `black` for formatting.
- **Commit Messages**: Use clear, descriptive commit messages. Follow the convention:

    ```
    type(scope): subject
    ```

    Where `type` can be `feat` (feature), `fix` (bug fix), `docs` (documentation), etc., and `scope` is optional but can be the file or feature the commit affects.

## License

By contributing to PythonAppGenerator-Template, you agree that your contributions will be licensed under the MIT License.

Thank you for your contributions!