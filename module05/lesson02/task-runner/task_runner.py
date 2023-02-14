import asyncio
from aiofile import async_open
from aiopath import AsyncPath


async def consumer(filename, queue: asyncio.Queue):
    async with async_open(filename, "w", encoding='utf-8') as afp:
        while True:
            file, data = await queue.get()
            print(f'operation with file {file.name}')
            await afp.write(f'{data}\n')
            queue.task_done()


async def producer(file: AsyncPath, queue: asyncio.Queue):
    async with async_open(file, 'r', encoding='utf-8') as fr:
        print(f'read file {file.name}')
        data = []
        async for line in fr:
            data.append(str(line))
        data_all = ''.join(data)
        await queue.put((file, data_all))
        print(f'completed read file {file.name}')


async def main():
    files = AsyncPath('.').joinpath('files').glob('*.js')
    print(files)
    queue_produce = asyncio.Queue()

    producers = [asyncio.create_task(producer(file, queue_produce)) async for file in files]
    task_consumer = asyncio.create_task(consumer('main.js', queue_produce))

    await asyncio.gather(*producers)
    await queue_produce.join()
    task_consumer.cancel()
    print('Completed')


if __name__ == '__main__':
    asyncio.run(main())
