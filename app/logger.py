import logging as log


# Logging
log.basicConfig(
    filename="logs/log.log",
    level=log.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)