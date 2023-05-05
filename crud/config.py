from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path, PurePath


class ConfigFile:
    path: PurePath
    type: str
    settings: ConfigParser

    def __init__(self, config_file) -> None:
        self.path = config_file
        self.type, self.settings = self._set_type(config_file)

    def _set_type(self, config_file):
        match PurePath(config_file).suffix[1:].lower():
            case "ini":
                return ("INI", self._parse_ini(config_file))
            case _:
                print("bad file type found")

    def _parse_ini(self, config_file):
        parser = ConfigParser(interpolation=ExtendedInterpolation())
        parser.read(config_file)

        return parser


def configure_app(config_file):
    if not Path(config_file).exists():
        raise FileNotFoundError(f"Bad config file: {config_file}")

    return ConfigFile(config_file)
