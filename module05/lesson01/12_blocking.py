import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def io_operation():
    with open('../main.py', 'r') as f:
        return f.read(100)


def cpu_operation(power: int, p: int):
    r = [i ** power for i in range(10 ** p)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    r = await loop.run_in_executor(None, io_operation)
    print(r)

    r = await loop.run_in_executor(None, cpu_operation, 2, 6)
    print(r)

    with ThreadPoolExecutor() as pool:
        r = await loop.run_in_executor(pool, io_operation)
        print(r)

    with ProcessPoolExecutor() as pool:
        r = await loop.run_in_executor(pool, cpu_operation, 2, 6)
        print(r)


if __name__ == '__main__':
    asyncio.run(main())
