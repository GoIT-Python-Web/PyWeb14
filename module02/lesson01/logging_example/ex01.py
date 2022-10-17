import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(funcName)15s - %(message)s"
)


def foo(num: int):
    baz = 10
    result = num + baz
    logging.debug(f"result={result}")
    return result


if __name__ == "__main__":
    foo(3)
