import asyncio
from time import time


async def send_metrics(url) -> None:
    print(f'Send to {url}: {time()}')


async def worker():
    while True:
        await asyncio.sleep(1)
        await send_metrics('https://to.me')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(worker())
    loop.run_forever()
    # asyncio.run(worker())


