import logging
import os
logger = logging.getLogger(__name__)

class BaseCommand():
    cmd: str

    def __init__(self):
        logger.info(f"Initalizing object: BaseCommand")

    def validate_config(self):
        logger.info(f"blah")

        # Confirm config works
        logger.info(f"conf_file source: {self.config['DEFAULTS']['SOURCE']}")
        try:
            logger.info(f"env_file source: {os.environ['SOURCE']}")
        except KeyError:
            logger.error("Env var SOURCE does not exist")

    def execute(self):
        pass
    