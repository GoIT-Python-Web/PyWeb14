import logging
from logger import get_logger

logger = get_logger(__name__)


def baz():
    b = 10
    logger.info("Start baz")
    logger.debug(f"b={b}")


def foo():
    logger.error("Ups i did it again")


if __name__ == "__main__":
    logger.log(logging.DEBUG, "Start")
    baz()
    foo()
