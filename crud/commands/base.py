import logging
import os

logger = logging.getLogger(__name__)


class BaseCommand:
    cmd: str

    def __init__(self) -> None:
        logger.info("Initalizing object: BaseCommand")

    def validate_config(self) -> None:
        # Confirm config works
        try:
            logger.debug(f"env_file source: {os.environ['SOURCE']}")
        except KeyError:
            logger.error("Env var SOURCE does not exist")

    def execute(self) -> None:
        pass
