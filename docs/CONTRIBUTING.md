
## Examples

```bash
# See options
poetry run cli-command

# Execute 'create' command
poetry run cli-command -c configs/config.ini create 

# Execute 'create' command with .env file
poetry run cli-command -c configs/config.ini -e configs/dev.env create

# Execute 'read' command and pass parameter
poetry run cli-command -c configs/config.ini -e configs/dev.env read -f file_to_read.txt
```