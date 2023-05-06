
# Overview

# Install

# Use

## Examples

```bash
# See options
poetry run cli-command

# Execute 'create' command
poetry run cli-command -c configs/config.ini create 

# Execute 'create' command with .env file
poetry run cli-command -c configs/config.ini -e configs/dev.env create
```

# Configure

# Contribute

```bash
# lint
poetry run pre-commit run --all-files
```