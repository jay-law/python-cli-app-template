import logging
import logging.config
from pathlib import PurePath

import click

from crud.commands.factory import CmdFactory
from crud.config import configure_app

logger = logging.getLogger(__name__)


def configure_logging(config_file=PurePath("configs", "logging.ini"), log_level=str):
    logging.config.fileConfig(config_file, disable_existing_loggers=False)

    if log_level is not None:
        for handler in logging.getLogger().handlers:
            handler.setLevel(log_level)


@click.group
@click.option("-v", "--verbose", "log_level", flag_value="DEBUG")
@click.option("-q", "--quiet", "log_level", flag_value="CRITICAL")
@click.option("-c", "--config", "config_file", type=str, required=True)
@click.option("-e", "--environment", "env_file", type=str)
@click.pass_context
def cli(ctx, log_level, config_file, env_file):
    config_parser = configure_app(config_file, env_file)

    configure_logging(log_level=log_level)

    # params made available to cli.commands
    ctx.ensure_object(dict)
    ctx.obj["config"] = config_parser.settings

    pass


@cli.command()
@click.pass_context
def create(ctx):
    cmd = CmdFactory.generate_command(cmd="create", config=ctx.obj["config"])
    cmd.validate_config()
    cmd.execute()


@cli.command()
@click.pass_context
@click.option("-f", "--file", "file", type=str)
def read(ctx, file):
    cmd = CmdFactory.generate_command(cmd="read", config=ctx.obj["config"])
    cmd.validate_config()
    cmd.execute(file)


@cli.command()
@click.pass_context
def update(ctx):
    cmd = CmdFactory.generate_command(cmd="update", config=ctx.obj["config"])
    cmd.validate_config()
    cmd.execute()


@cli.command()
@click.pass_context
def delete(ctx):
    cmd = CmdFactory.generate_command(cmd="delete", config=ctx.obj["config"])
    cmd.validate_config()
    cmd.execute()


def main():
    cli()


if __name__ == "__main__":
    main()
