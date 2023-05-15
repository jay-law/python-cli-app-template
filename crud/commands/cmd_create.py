import logging

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class CreateCmd(BaseCommand):
    cmd: str = "create"

    def __init__(self) -> None:
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self) -> None:
        logger.info(f"Executing command: {self.cmd}")
