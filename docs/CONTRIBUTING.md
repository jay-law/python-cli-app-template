
# Execution

## Examples

```bash
# See options
poetry run cli-command

# Execute 'create' command
poetry run cli-command create

# Execute 'create' command with .env file
poetry run cli-command -e configs/dev.env create

# Execute 'read' command and pass parameter
poetry run cli-command -e configs/dev.env read -f file_to_read.txt
```

# Packaging

```bash
# Create executable
poetry run pyinstaller crud/cli.py --onefile
# Creates dist/cli
```