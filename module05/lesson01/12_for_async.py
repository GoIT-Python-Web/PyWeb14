import asyncio
from time import sleep, time
from typing import Iterable, Awaitable, AsyncIterator

from faker import Faker

from libs import async_timed

fake = Faker()


async def get_user_async(uuid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users(uuids: list[int]) -> AsyncIterator:
    for uuid in uuids:
        yield get_user_async(uuid)


@async_timed()
async def main(users: AsyncIterator):
    result = []
    async for user in users:
        result.append(user)
    return await asyncio.gather(*result)


if __name__ == '__main__':

    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)





