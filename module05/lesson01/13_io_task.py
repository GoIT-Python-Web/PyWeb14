import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import time

import requests

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com',
        'http://www.python.org', 'http://duckduckgo.com', 'http://www.google.com', 'http://www.python.org',
        'http://ttt.ttt']


def get_url(url):  # blocking IO operation
    r = requests.get(url)
    return url, r.text[:100]


async def get_url_async():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(3) as pool:
        features = [loop.run_in_executor(pool, get_url, url) for url in urls]
        r = await asyncio.gather(*features, return_exceptions=False)
        print(r)


if __name__ == '__main__':
    start = time()
    asyncio.run(get_url_async())
    print(time() - start)

    start = time()
    results = []
    for url in urls:
        try:
            results.append(get_url(url))
        except Exception as err:
            print(err)
    print(results)
    print(time() - start)
