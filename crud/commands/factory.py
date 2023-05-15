import logging

from crud.commands.cmd_create import CreateCmd
from crud.commands.cmd_delete import DeleteCmd
from crud.commands.cmd_read import ReadCmd
from crud.commands.cmd_update import UpdateCmd

logger = logging.getLogger(__name__)


class BadCommandRequested(Exception):
    pass


class CmdFactory:
    @staticmethod
    def generate_command(cmd: str):
        match cmd:
            case "create":
                return CreateCmd()
            case "read":
                return ReadCmd()
            case "update":
                return UpdateCmd()
            case "delete":
                return DeleteCmd()
            case _:
                raise BadCommandRequested(f"Bad command of: {cmd}")
