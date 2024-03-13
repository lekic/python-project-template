# Python Python Template

This repo provides a python template with best-practices and useful tools for your workflow.

## Features

### Development

* [Dependabot] for vulnerability management
* [Development Containers] for containerised environment setup
* [GitHub Actions] for CI/CD and testing of the repository
* GitHub issue templates, pull request templates, and `CODEOWNERS` file
* [pre-commit] hooks for commit validation

### Python

* General best-practice repo structure: `docs`, `src`, `tests`
* [mypy] for static type checking
* [pytest] for unit testing, including `pytest-cov` to measure coverage
* [ruff] for linting and formatting (replaces/integrates `black`, `flake8`, `isort`, `pyupgrade`)
* [setuptools] for build management and distribution using `pyproject.toml`
* [tox] for multi-environment Python testing

## Development

This repository supports building and testing in multiple Python versions, however, the devcontainer is set to Python 3.10 by default. To change this, update the `VARIANT` argument in `.devcontainer/devcontainer.json` and `.devcontainer/Dockerfile`.

## Development instructions

### With devcontainer

This repository comes with a devcontainer (a Dockerized Python environment). If you open it in Codespaces, it should automatically initialize the devcontainer.

Locally, you can open it in VS Code with the Dev Containers extension installed.

### Without devcontainer

If you can't or don't want to use the devcontainer, then you should first create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev tools and pre-commit hooks:

```bash
python3 -m pip install -r requirements-dev.txt
pre-commit install
```

## File breakdown

Here's a short explanation of key files and folders in this template:

* `.devcontainer`: Folder containing config files to build development environment
* `.github`: Folder for GitHub specific files, templates and actions
* `docs`: Placeholder destination folder for generating code documentation
* `src`: The main application code folder
* `tests`: Folder containing Python tests
* `.gitignore`: File describing what file patterns Git should never track
* `.markdownlint.yml`: Markdown linting config file
* `.pre-commit-config.yaml`: File listing all the pre-commit hooks and args
* `CHANGELOG.md`: Template changelog file for those looking to maintain one
* `CONTRIBUTING.md`: General contribution guidelines for this project
* `pyproject.toml`: File configuring Python build and most of the dev tools
* `requirements-dev.txt`: File listing all PyPi packages required for development
* `requirements.txt`: File listing all PyPi packages required for production
* `tox.ini`: File for configuring tox automated Python testing

## Reference Material

Below are some of the useful links that have influenced the template project

* [Good Integration Practices - pytest documentation]
* [How Do I Set Up a Python Project]
* [Python Packaging User Guide]
* [Setting Your Python Project Up for Success in 2024]

## Contributions

Feel free to raise any issues or pull requests to improve the template.

<!-- Links -->
[Dependabot]: https://github.com/dependabot
[Development Containers]: https://containers.dev/
[GitHub Actions]: https://github.com/features/actions
[Good Integration Practices - pytest documentation]: https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html
[How Do I Set Up a Python Project]: http://blog.pamelafox.org/2022/09/how-i-setup-python-project.html
[Python Packaging User Guide]: https://packaging.python.org/en/latest/
[Setting Your Python Project Up for Success in 2024]: https://medium.com/@Mr_Pepe/setting-your-python-project-up-for-success-in-2024-365e53f7f31e
[mypy]: https://mypy-lang.org/
[pre-commit]: https://pre-commit.com/
[pytest]: https://pytest.org/
[ruff]: https://docs.astral.sh/ruff/
[setuptools]: https://setuptools.pypa.io/en/latest/
[tox]: https://tox.wiki/en/latest/