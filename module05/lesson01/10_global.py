import asyncio

global_name = None


async def task_one(name: str):
    global global_name
    print(f'My name {name}: {global_name}')
    global_name = name
    print(f'My name {name}: {global_name}')


async def main():
    await asyncio.gather(*[task_one(name) for name in ['Morey', 'Elza', 'Jina']])


if __name__ == '__main__':
    asyncio.run(main())