import asyncio
import random
import queue


async def producer(queue: asyncio.Queue):
    num = random.randint(1, 100)
    await asyncio.sleep(0.3)
    await queue.put(num)


async def consumer(queue_produce: asyncio.Queue, queue_result: queue.Queue):
    while True:
        num = await queue_produce.get()
        result = num ** 2
        queue_result.put((num, result))
        queue_produce.task_done()


async def main():
    queue_produce = asyncio.Queue()
    queue_result = queue.Queue()
    consumers = [asyncio.create_task(consumer(queue_produce, queue_result)) for _ in range(5)]
    producers = [asyncio.create_task(producer(queue_produce)) for _ in range(10)]
    await asyncio.gather(*producers)
    await queue_produce.join()
    [consume.cancel() for consume in consumers]
    return queue_result


if __name__ == '__main__':
    r = asyncio.run(main())
    while not r.empty():
        print(r.get())
