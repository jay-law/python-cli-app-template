from crud.commands.cmd_create import CreateCmd
import logging

logger = logging.getLogger(__name__)

class BadCommandRequested(Exception):
    pass

class CmdFactory:

    @staticmethod
    def generate_command(cmd: str, config):
        match cmd:
            case 'create':
                return CreateCmd(config)
            case _:
                raise BadCommandRequested(f"Bad command of: {cmd}")
