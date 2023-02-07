import asyncio


async def baz():
    print('Before sleep')
    await asyncio.sleep(1)
    print('After sleep')
    return 'Hello world!'


async def main() -> None:
    r = baz()
    print(r)  # coroutine
    result = await r  # result
    print(result)


if __name__ == '__main__':
    asyncio.run(main())

