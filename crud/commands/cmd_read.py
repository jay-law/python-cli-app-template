import logging
from pathlib import PurePath

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class ReadCmd(BaseCommand):
    cmd: str = "read"

    def __init__(self) -> None:
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self) -> None:
        logger.info(f"Executing command: {self.cmd}")

    def read(self, file: PurePath) -> None:
        logger.info(f"Reading file: {file}")
