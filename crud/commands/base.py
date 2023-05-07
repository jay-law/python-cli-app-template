import logging
import os

logger = logging.getLogger(__name__)


class BaseCommand:
    cmd: str

    def __init__(self):
        logger.info("Initalizing object: BaseCommand")

    def validate_config(self):
        # Confirm config works
        logger.debug(f"conf_file source: {self.config['DEFAULTS']['SOURCE']}")
        try:
            logger.debug(f"env_file source: {os.environ['SOURCE']}")
        except KeyError:
            logger.error("Env var SOURCE does not exist")

    def execute(self):
        pass
