import logging

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class ReadCmd(BaseCommand):
    cmd: str = "read"

    def __init__(self) -> None:
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self, file) -> None:
        logger.info(f"Executing command: {self.cmd}")
        logger.info(f"Reading file: {file}")
