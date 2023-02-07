from asyncio import Future
import asyncio
from time import time

from faker import Faker

fake = Faker()


async def get_user_async(uid: int, future: Future) -> None:
    await asyncio.sleep(0.5)
    future.set_result({'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()})


def make_request(uuid: int) -> Future:
    future = Future()
    asyncio.create_task(get_user_async(uuid, future))
    return future


async def main():
    u1_future = make_request(1)
    u2_future = make_request(2)
    u3_future = make_request(3)
    print(u1_future, u2_future, u3_future)
    print(u1_future.done(), u2_future.done(), u3_future.done())
    r = await asyncio.gather(u1_future, u2_future, u3_future)
    print(u1_future.done(), u2_future.done(), u3_future.done())
    return r


if __name__ == '__main__':
    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)
