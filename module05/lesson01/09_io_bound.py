import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import time
from typing import List

import requests
from requests.exceptions import MissingSchema, RequestException

from libs import async_timed

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com',
        'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com', 'http://www.python.org/fake', 'ttt']


def get_url(url: str) -> (str, str):  # blocking IO operation
    r = requests.get(url)
    return url, r.text[:100]


@async_timed()
async def get_url_async():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(3) as pool:
        features = [loop.run_in_executor(pool, get_url, url) for url in urls]
        r = await asyncio.gather(*features, return_exceptions=True)
        print(r)


if __name__ == '__main__':
    asyncio.run(get_url_async())

    start = time()
    results = []
    for url in urls:
        try:
            results.append(get_url(url))
        except MissingSchema as err:
            print(err)
    print(results)
    print(time() - start)
