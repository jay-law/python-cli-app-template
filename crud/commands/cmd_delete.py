import logging

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class DeleteCmd(BaseCommand):
    cmd: str = "delete"

    def __init__(self) -> None:
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self) -> None:
        logger.info(f"Executing command: {self.cmd}")
