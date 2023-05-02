from configparser import ConfigParser, ExtendedInterpolation
from pathlib import PurePath


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
            case _:
                print("bad file type found")

    def _parse_ini(self, config_file):
        parser = ConfigParser(interpolation=ExtendedInterpolation())
        parser.read(config_file)

        # Convert to dict
        dict_format = {}
        for section in parser.sections():
            dict_format[section] = dict(parser[section])

        return dict_format


def configure_app(config_file):
    if config_file is None:
        print("No config file provided")
        return

    return ConfigFile(config_file)
