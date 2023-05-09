
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

# Installing

```bash
# Download
wget https://github.com/jay-law/python-crud-template/releases/download/0.1.6/crud-cli-linux-0.1.6.tar.gz

# Uncompress
tar -xvf crud-cli-linux-0.1.6.tar.gz
```

# Using

```bash
# Execute
./cli -c /home/jon/Documents/repos/personal/python-crud-template/configs/config.ini create
```

# Configuring

# Contributing

See `docs/CONTRIBUTING.md`

```bash
# lint
poetry run pre-commit run --all-files
```