import platform
from datetime import datetime
import logging

import aiohttp
import asyncio


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    r = await resp.json()
                    return r
                logging.error(f"Error status: {resp.status} for {url}")
                return None
        except aiohttp.ClientConnectorError as err:
            logging.error(f"Connection error: {str(err)}")
            return None


async def get_exchange():
    result = await request('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    if result:
        exc, = list(filter(lambda el: el["ccy"] == "USD", result))
        return f"USD: buy: {exc['buy']}, sale: {exc['sale']}. Date: {datetime.now().date()}"
    return "Failed to retrieve data"


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    result = asyncio.run(get_exchange())
    print(result)
