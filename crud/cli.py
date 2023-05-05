import logging
from pathlib import PurePath

import click

from crud.config import configure_app
from crud.log import configure_logging

logger = logging.getLogger(__name__)


@click.group
@click.option(
    "-v",
    "--verbosity",
    "log_level",
    default="INFO",
    type=click.Choice(
        ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        case_sensitive=False,
    ),
)
@click.option("-c", "--config", "config_file", type=str)
@click.option(
    "-l",
    "--log",
    "log_file",
    type=str,
    default=lambda: PurePath(PurePath(__file__).parent.parent, "logs"),
)
@click.pass_context
def cli(ctx, log_level, config_file, log_file):
    config = configure_app(config_file)
    configure_logging(log_level)

    ctx.ensure_object(dict)
    ctx.obj["settings"] = config.settings

    pass


@cli.command()
@click.pass_context
def create(ctx):
    logger.info("create command")
    logger.info(f"settings: {ctx.obj['settings']}")


@cli.command()
@click.pass_context
def read(ctx):
    logger.info("read command")


@cli.command()
@click.pass_context
def update(ctx):
    logger.info("update command")


@cli.command()
@click.pass_context
def delete(ctx):
    logger.info("delete command")


def main():
    cli()


if __name__ == "__main__":
    main()
