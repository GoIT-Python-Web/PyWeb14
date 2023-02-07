import asyncio
from time import sleep, time
from typing import Coroutine, List, Any

from faker import Faker

fake = Faker()


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_users(uids: List[int]) -> list[Coroutine[Any, dict, Any]]:
    return [get_user_async(i) for i in uids]


async def main(users: Coroutine[Any, list[Coroutine[Any, Any, dict]], Any]):
    result = []
    for user in await users:
        result.append(user)
    return await asyncio.gather(*result)


if __name__ == '__main__':
    uids = [1, 2, 3]
    start = time()
    r = asyncio.run(main(get_users(uids)))
    print(r)
    print(time() - start)
