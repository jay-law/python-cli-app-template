from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path, PurePath

from dotenv import dotenv_values, load_dotenv


class ConfigFile:
    path: PurePath
    type: str

    def __init__(self, config_file) -> None:
        self.path = config_file
        self.type, self.settings = self._set_type(config_file)

    def _set_type(self, config_file):
        match PurePath(config_file).suffix[1:].lower():
            case "ini":
                return ("INI", self._parse_ini(config_file))
            case "env":
                return ("ENV", self._load_env(config_file))
            case _:
                print("bad file type found")

    def _parse_ini(self, config_file):
        parser = ConfigParser(interpolation=ExtendedInterpolation())
        parser.read(config_file)

        return parser

    def _load_env(self, env_file):
        load_dotenv(env_file)
        return dotenv_values(env_file)


def configure_app(config_file, env_file):
    if not Path(config_file).exists():
        raise FileNotFoundError(f"Bad file: {config_file}")

    if env_file is not None:
        if not Path(env_file).exists():
            raise FileNotFoundError(f"Bad file: {env_file}")
        ConfigFile(env_file)

    return ConfigFile(config_file)
