import asyncio
from time import sleep, time
from typing import Coroutine, List, Any

from faker import Faker

from libs import async_timed

fake = Faker()


async def get_user_async(uuid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users(uuids: List[int]) -> list[Coroutine[Any, dict, Any]]:
    return [get_user_async(i) for i in uuids]


@async_timed()
async def main(users: Coroutine[Any, list[Coroutine[Any, Any, dict]], Any]):
    result = []
    for user in await users:
        result.append(user)
    return await asyncio.gather(*result)


if __name__ == '__main__':
    uuids = [1, 2, 3]
    r = asyncio.run(main(get_users(uuids)))
    print(r)

