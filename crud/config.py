import logging
import sys
from configparser import ConfigParser, ExtendedInterpolation
from pathlib import Path, PurePath

from dotenv import load_dotenv

logger = logging.getLogger(__name__)


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
                logging.error(f"Bad config file type provided: {config_file}")
                sys.exit(1)

    def _load_env(self, env_file):
        load_dotenv(env_file)

    def _parse_ini(self, ini_file):
        parser = ConfigParser(interpolation=ExtendedInterpolation())
        parser.read(ini_file)

        return parser


def configure_app(env_file):
    if not Path(env_file).exists():
        logging.error(f"Bad file provided: {env_file}")
        sys.exit(1)
    ConfigFile(env_file)
