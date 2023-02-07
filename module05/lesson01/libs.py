from functools import wraps
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'Виконується {func.__name__} з аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func.__name__} завершила виконання за {total:.4f} с')

        return wrapped

    return wrapper
