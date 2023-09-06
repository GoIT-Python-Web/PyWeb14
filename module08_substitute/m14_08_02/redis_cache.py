import timeit

import redis
from redis_lru import RedisLRU


client = redis.Redis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@cache
def fib_cache(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)


if __name__ == '__main__':
    start_time = timeit.default_timer()
    r = fib(35)
    print(f"fib = {r}: {timeit.default_timer() -  start_time}")


    start_time = timeit.default_timer()
    r = fib_cache(350)
    print(f"fib = {r}: {timeit.default_timer() -  start_time}")
