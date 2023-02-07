import asyncio
from time import sleep, time

from faker import Faker

fake = Faker()


async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def main():
    u1_task = asyncio.create_task(get_user_async(1))
    u2_task = asyncio.create_task(get_user_async(2))
    u3_task = asyncio.create_task(get_user_async(3))
    print(u1_task, u2_task, u3_task)
    user1 = await u1_task
    user2 = await u2_task
    user3 = await u3_task
    return user1, user2, user3


if __name__ == '__main__':
    start = time()
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # r = loop.run_until_complete(main())
    r = asyncio.run(main())
    print(r)
    print(time() - start)
    # loop.close()

