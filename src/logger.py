import logging as log
from logging.config import dictConfig


dictConfig(
    {
        "version": 1,
        "formatters": {
            "precise": {
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(module)s | %(message)s"
            },
            "brief": {"format": "%(asctime)s | %(levelname)s | %(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "brief",
                "level": "WARNING",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "precise",
                "filename": "logs/api.log",
                "maxBytes": 1024 ** 2,  # 1 Mb
                "backupCount": 1,
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)
