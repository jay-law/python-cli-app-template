import logging

from crud.commands.base import BaseCommand

logger = logging.getLogger(__name__)


class CreateCmd(BaseCommand):
    cmd: str = "create"

    def __init__(self):
        super().__init__()
        logger.info(f"Initalizing command: {self.cmd}")

    def execute(self):
        logger.info(f"Executing command: {self.cmd}")
