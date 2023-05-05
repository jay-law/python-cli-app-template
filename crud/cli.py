import logging
import logging.config

import click

from crud.config import configure_app

logger = logging.getLogger(__name__)


def configure_logging(config_file, verbose):
    logging.config.fileConfig(config_file, disable_existing_loggers=False)

    if verbose:
        logger.info("Verbose logging enabled")
        for handler in logging.getLogger().handlers:
            handler.setLevel("DEBUG")


@click.group
@click.option("-v", "--verbose", is_flag=True)
@click.option("-c", "--config", "config_file", type=str)
@click.pass_context
def cli(ctx, verbose, config_file):
    config = configure_app(config_file)

    configure_logging(config_file, verbose)

    # params made available to cli.commands
    ctx.ensure_object(dict)
    ctx.obj["settings"] = config.settings

    pass


@cli.command()
@click.pass_context
def create(ctx):
    logger.info("create command")

    settings = ctx.obj["settings"]

    for section in settings.sections():
        print(f"{dict(settings[section])}")


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
