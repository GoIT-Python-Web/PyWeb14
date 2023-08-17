import asyncio
from time import sleep, time

from faker import Faker

fake = Faker()


def get_user_sync(uid: int) -> dict:
    sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


async def get_user_async(uid: int) -> dict:
    initial_data = {'id': uid, 'name': fake.name(), 'company': fake.company()}
    # simulate request
    asyncio.sleep(0.5)
    initial_data['email']= fake.email()
    yield initial_data

async def main():
    list_of_tasks = [
        get_user_async(1),
        get_user_async(2),
        get_user_async(3),
        get_user_async(11),
        get_user_async(12),
        get_user_async(13),
        get_user_async(14),

    ]

    r = await asyncio.gather(
        *list_of_tasks
    )
    return r


if __name__ == '__main__':
    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)
    print('------------------------------')
   