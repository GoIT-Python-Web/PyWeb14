import logging
from logging import WARNING
from typing import Union

from ex02 import baz

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(funcName)15s - %(message)s"
)


def foo(num: list[list[str]]) -> list[int]:
    baz = 10
    result = [num, baz]
    logging.debug(f"result={result}")
    return result


if __name__ == "__main__":
    foo("3")
