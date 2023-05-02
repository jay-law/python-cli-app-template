import logging
import logging.config

# import logging.handlers
from pathlib import PurePath

logger = logging.getLogger(__name__)

ROOT_DIR = PurePath(__file__).parent.parent
LOGS_DIR = PurePath(ROOT_DIR, "logs")


DEFAULT_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "detailed": {
            "class": "logging.Formatter",
            "format": "[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": PurePath(LOGS_DIR, "crud.log"),
            "mode": "w+",
            "level": "INFO",
            "formatter": "detailed",
        },
    },
    "loggers": {"root": {"level": "DEBUG", "handlers": ["console", "file"]}},
}


def configure_logging(log_level="INFO") -> None:
    logging.config.dictConfig(DEFAULT_LOGGING)
    logger.info("info in log.py")

    if log_level is not None:
        logger.info(f"Setting log level to {log_level}")
        for handler in logging.getLogger().handlers:
            handler.setLevel(log_level)
