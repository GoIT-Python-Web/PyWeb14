import asyncio
from time import sleep, time

from faker import Faker

fake = Faker()


def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def main():
    r = await asyncio.gather(
        get_user_async(1),
        get_user_async(2),
        get_user_async(3)
    )
    return r


if __name__ == '__main__':
    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)
    print('------------------------------')
    start = time()
    user4 = get_user_sync(4)
    user5 = get_user_sync(5)
    user6 = get_user_sync(6)
    print(user4, user5, user6)
    print(time() - start)
