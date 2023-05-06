import logging
import logging.config
import os
from pathlib import PurePath

import click

from crud.config import configure_app

logger = logging.getLogger(__name__)


def configure_logging(config_file=PurePath("configs", "logging.ini"), verbose=False):
    logging.config.fileConfig(config_file, disable_existing_loggers=False)

    if verbose:
        logger.info("Verbose logging enabled")
        for handler in logging.getLogger().handlers:
            handler.setLevel("DEBUG")


@click.group
@click.option("-v", "--verbose_flg", is_flag=True)
@click.option("-c", "--config", "config_file", type=str, required=True)
@click.option("-e", "--environment", "env_file", type=str)
@click.pass_context
def cli(ctx, verbose_flg, config_file, env_file):
    config = configure_app(config_file, env_file)

    configure_logging(verbose=verbose_flg)

    # params made available to cli.commands
    ctx.ensure_object(dict)
    ctx.obj["settings"] = config.settings

    pass


@cli.command()
@click.pass_context
def create(ctx):
    logger.info("create command")

    settings = ctx.obj["settings"]

    # Confirm config works
    logger.info(f"conf_file source: {settings['DEFAULTS']['SOURCE']}")
    try:
        logger.info(f"env_file source: {os.environ['SOURCE']}")
    except KeyError:
        logger.error("Env var SOURCE does not exist")


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
