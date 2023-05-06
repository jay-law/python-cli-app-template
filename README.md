
# CRUDy Python Template

Temaplte for rapid development for small Python CLI apps.

Allows expansion of core functionality like:
- Creation of commands like create, read, etc.
- Creation of command arguments like "read --file file_to_read.txt"
- Creation of global arguments like verbose logging

Implements the following:
- Logging to stdout and log file
- Reading .ini config files
- Setting env vars with .env files

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