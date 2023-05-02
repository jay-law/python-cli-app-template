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
def cli(log_level, config_file, log_file):
    configure_app(config_file)
    configure_logging(log_level)

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

    pass


@cli.command()
def create():
    logger.info("create command")



@cli.command()
def read():
    logger.info("read command")


@cli.command()
def update():
    logger.info("update command")


@cli.command()
def delete():
    logger.info("delete command")


def main():
    cli()


if __name__ == "__main__":
    main()
