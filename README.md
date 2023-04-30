# Recreate Template

Commands to recreate this template from scratch.

First, create the repo in GitHub and clone locally.

```bash
# Create pyproject.toml file
poetry init
# Use default for all except for defining dependencies.  Hit n for those

# Build out project
mkdir python_cli_app_template
touch  python_cli_app_template/__init__.py

# Populate __init__.py
echo "print('Hello World')" > python_cli_app_template/__init__.py

# Test by executing v1
python3 python_cli_app_template/__init__.py

# Test by executing v2
poetry run python3 python_cli_app_template/__init__.py 
```

## Linters and Formatters

```bash
# Configure Poetry to add venv inside the project
poetry config virtualenvs.in-project true

# Add linters and formatters as dev dependencies
poetry add -G dev black isort flake8 mypy

# Test black
poetry run black python_cli_app_template

# Test isort
poetry run isort .

# Test flake8
poetry run flake8 python_cli_app_template

# Test mypy
poetry run mypy python_cli_app_template

# Update pyproject.toml by adding the following lines to the end
cat << EOF >> pyproject.toml

[tool.black]
line-length = 79

[tool.isort]
profile = "black"
line_length = 80
EOF

```

## Pre-Commit

```bash
# Add pre-commit as dev dependencies
poetry add -G dev pre-commit

# Configure pre-commit with linters and formatters
cat << EOF > .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: black
        name: black
        entry: poetry run black python_cli_app_template
        always_run: true
        language: system
        pass_filenames: false
      - id: isort
        name: isort
        entry: poetry run isort .
        always_run: true
        language: system
        pass_filenames: false  
      - id: flake8
        name: flake8
        entry: poetry run flake8 python_cli_app_template
        always_run: true
        language: system
        pass_filenames: false     
      - id: mypy
        name: mypy
        entry: poetry run mypy python_cli_app_template
        always_run: true
        language: system
        pass_filenames: false
EOF

# Run pre-commit on all files
poetry run pre-commit run --all-files

# Install commit hooks
poetry run pre-commit install

# Push changes
```

# Functionality


## Add Poetry Script

```bash

echo "print('Hello World')" > python_cli_app_template/__init__.py

# Update __init__.py - add main()
cat << EOF > python_cli_app_template/__init__.py
def main():
    print("Hello World")
EOF

# Update pyproject.toml - add script
cat << EOF >> pyproject.toml

[tool.poetry.scripts]
cli-command = "python_cli_app_template:main"
EOF

# Execute
poetry run cli-command
```

## Click

```bash
# Add click
poetry add click

# Clear __init__.py



```

# Git

## Push Changes

```bash
# Increment version
poetry version patch

# Add files to commit
git add .

# Commit changes
git commit -m 'initial commit'
# The pre-commit hook will be triggered

# Push changes
git push
```

