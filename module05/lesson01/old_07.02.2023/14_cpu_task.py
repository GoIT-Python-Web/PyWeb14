import asyncio
import concurrent.futures
import datetime


def cpu_blocking_task(counter):
    init = counter
    while counter > 0:
        counter -= 1
    print(f'completed cpu_blocking_task {init}')
    return f'completed cpu_blocking_task {init}'


async def async_process_worker():
    loop = asyncio.get_event_loop()
    loop.create_task(ticker())
    with concurrent.futures.ProcessPoolExecutor(2) as executor:
        futures = [loop.run_in_executor(executor, cpu_blocking_task, n) for n in [50_000_000, 60_000_000, 70_000_000]]
        results = await asyncio.gather(*futures)
        return results


async def ticker():
    while True:
        print(datetime.datetime.now())
        await asyncio.sleep(1)


async def main():
    res = ' '.join(await async_process_worker())
    return res


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)

