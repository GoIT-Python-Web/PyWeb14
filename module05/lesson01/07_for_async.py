import asyncio
from time import sleep, time
from typing import Iterable, Awaitable, AsyncIterator

from faker import Faker

fake = Faker()


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users(uids: list[int]) -> AsyncIterator:
    for uid in uids:
        yield get_user_async(uid)


async def main(users: AsyncIterator):
    result = []
    async for user in users:
        result.append(user)
    return await asyncio.gather(*result)


if __name__ == '__main__':
    start = time()
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
    print(time() - start)




