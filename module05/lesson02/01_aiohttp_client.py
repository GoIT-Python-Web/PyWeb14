import aiohttp
import asyncio
import platform

urls = ['https://www.google.com', 'https://www.python.org/asdf', 'https://duckduckgo.com', 'http://test']


async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            print(f'Starting {url}')
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        html = await resp.text()
                        print(url, html[:150])
                    else:
                        print(f"Error status: {resp.status} for {url}")
            except aiohttp.ClientConnectorError as err:
                print(f'Connection error: {url}', str(err))


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
