<center>
    <img src="docs/logo.png" alt="drawing" width="200px"/>
</center>

> _This repo structure has been autogenerated from [Intellectual Labs cookiecutter template](https://github.com/IntellectualLabs/data_science_template).
> Feel free to change the company logo under `docs/images/CompanyLogo.png`_

# factorymind

Python module `factorymind` for the FactoryMind platform

_Explain the purpose of your repository/project here_

<!-- TOC -->

- [factorymind](#cookiecutterproject_name)
  - [1. Setup](#1-setup)
    - [1.1 Precommit](#11-precommit)
  - [2. Testing](#3-testing)
  - [3. References](#5-references)
  <!-- /TOC -->

## 1. Setup

_The setup shows how to set up your environment with the `poetry` python package manager_.

1. Install git and checkout the [git code repository](https://github.com/IntellectualLabs/template_data_science/).
2. Install [Poetry]: <https://python-poetry.org/docs/#installation>
3. Change working directory into the git code repository root
4. Create the self contained environment;

   - _(If the config file `pyproject.toml` does not exist, initialize the environment file `poetry init`.)_
   - Create the env `poetry install`
   - Activate poetry shell `poetry shell`
   - Add packages by `poetry add <package>`.
     - add package as dev package `--dev (-D)`, e.g. `poetry add -D ipykernel` (_already included_)
     - install without dev dependencies `poetry install --no-dev`
   - Update `poetry.lock` without upgrading dependencies: `poetry lock --no-update`

#### Installation issues

- If you have any issues installing any python packages
  - especially wheels, try to update pip: `pip install --upgrade pip`
  - Or try upgrading your poetry version: `poetry self update`

### 1.1 Precommit

#### Setup

- `pip install pre-commit` (already installed in poetry env by default)
- Install the git hook scripts in `.pre-commit-config.yaml`:
  ```
  pre-commit install
  ```
- detect secrets setup
  - `detect-secrets scan > .secrets.baseline`
- auto update: `pre-commit autoupdate`

#### Usage

- `pre-commit run --all-files`

## 2. Testing

Reproducability and the correct functioning of code are essential to avoid wasted time.
If a code block is copied more than once then it should be placed into a
common script / module under `src/` and unit tests added. The same applies for
any other non trivial code to ensure the correct functioning.

To run tests, ensure you have installed the conda environment as explained above
(from `conda_env.yml`) and activated it.
_If not, install `pytest`, `pytest-cookies`, `pytest-cov`,
`pytest-remotedata==0.3.2` using pip or conda._
Then from the repository root run

```bash
pytest tests\
```

To display test coverage of all source code in the folder `src/` run from repository root

```bash
pytest --cov-report term-missing --cov=src tests/
```

For more details, see the README in the folder `tests\`.

## 3. References

- https://github.com/IntellectualLabs/data_science_template
- http://docs.python-guide.org/en/latest/writing/structure/
- https://intellectuallabs.no/

[//]: #
[anaconda]: https://www.continuum.io/downloads
