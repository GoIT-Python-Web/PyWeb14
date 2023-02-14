import asyncio
import aiohttp
import platform

urls = ['http://www.google.com', 'http://www.python.org/asdf', 'http://duckduckgo.com', 'http://test']


async def main():
    session = aiohttp.ClientSession()
    for url in urls:
        print(f'Starting {url}')
        try:
            response = await session.get(url)
            if response.status == 200:
                data = await response.text()
                print(f'{url} bytes:{len(data)} {data[:200]}')
            else:
                print(f"Error status: {response.status} for {url}")
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))

    await session.close()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
