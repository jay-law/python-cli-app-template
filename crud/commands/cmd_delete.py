import logging

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class DeleteCmd(BaseCommand):
    cmd: str = "delete"

    def __init__(self):
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self):
        logger.info(f"Executing command: {self.cmd}")
