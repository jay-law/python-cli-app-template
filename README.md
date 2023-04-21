# python-cli-app-template

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
```

```bash
poetry version patch

git add .

git commit -m 'initial commit'
```