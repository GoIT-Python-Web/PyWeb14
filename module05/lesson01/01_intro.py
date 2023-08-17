import asyncio
import time


async def baz():
    await asyncio.sleep(1)
    print('Дякую, що зачекали!')
    return 1


async def main() -> str:
    cr = baz()
    print(cr)  # coroutine
    result = await cr  # result
    print(f'In function: {result}')
    return result


if __name__ == '__main__':
    msg = asyncio.run(main())
    print(f'In main process: {msg}')

