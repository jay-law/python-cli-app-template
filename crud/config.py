from pathlib import Path

def configure_app(config_file):
    print("Configuring app")

    if config_file is not None and Path(config_file).exists:
        print("Reading config file")
