from typing import Callable

import time


def add(a, b):
    result = a + b
    return result


def add_random(a, b, cb: Callable):
    time.sleep(2)
    result = a + b
    cb(result)


if __name__ == '__main__':
    print(add(5, 5))

    add_random(5, 5, print)
