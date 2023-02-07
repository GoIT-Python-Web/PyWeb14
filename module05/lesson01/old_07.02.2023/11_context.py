import asyncio
from contextvars import ContextVar

global_name: ContextVar[str | None] = ContextVar('global_name', default=None)


async def task_one(name: str):
    print(f'My name {task_one.__name__}: {global_name.get()}')
    global_name.set(name)
    print(f'My name {task_one.__name__}: {name}')


async def main():
    await asyncio.gather(*[task_one(name) for name in ['Morey', 'Elza', 'Jina']])

    
if __name__ == '__main__':
    asyncio.run(main())
