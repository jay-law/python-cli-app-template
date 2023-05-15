import logging
import logging.config
from pathlib import PurePath

import click

from crud.commands.factory import CmdFactory
from crud.config import configure_app

logger = logging.getLogger(__name__)


def configure_logging(log_level=str):

    log_level = 'INFO' if log_level is None else log_level
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


@click.group
@click.option("-v", "--verbose", "log_level", flag_value="DEBUG")
@click.option("-q", "--quiet", "log_level", flag_value="CRITICAL")
@click.option("-e", "--environment", "env_file", type=str)
@click.pass_context
def cli(ctx, log_level, env_file):

    if env_file is not None:
        configure_app(env_file)

    configure_logging(log_level)

    # params made available to cli.commands
    ctx.ensure_object(dict)
    ctx.obj["some_key"] = "some_value"

    pass


@cli.command()
@click.pass_context
def create(ctx):
    x = config=ctx.obj["some_key"]
    cmd = CmdFactory.generate_command(cmd="create")
    cmd.validate_config()
    cmd.execute()


@cli.command()
@click.pass_context
@click.option("-f", "--file", "file", type=str)
def read(ctx, file):
    x = config=ctx.obj["some_key"]
    cmd = CmdFactory.generate_command(cmd="read")
    cmd.validate_config()
    cmd.execute(file)


@cli.command()
@click.pass_context
def update(ctx):
    x = config=ctx.obj["some_key"]
    cmd = CmdFactory.generate_command(cmd="update")
    cmd.validate_config()
    cmd.execute()


@cli.command()
@click.pass_context
def delete(ctx):
    x = config=ctx.obj["some_key"]
    cmd = CmdFactory.generate_command(cmd="delete")
    cmd.validate_config()
    cmd.execute()


def main():
    cli()


if __name__ == "__main__":
    main()
