import platform
from datetime import datetime

import aiohttp
import asyncio


async def get_exchange():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') as resp:
                if resp.status == 200:
                    r = await resp.json()
                    exc, = list(filter(lambda el: el["ccy"] == "USD", r))
                else:
                    return f"Error status: {resp.status}"
                return f"USD: buy: {exc['buy']}, sale: {exc['sale']}. Date: {datetime.now()}"
        except aiohttp.ClientConnectorError as err:
            return f"Connection error: {str(err)}"


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    result = asyncio.run(get_exchange())
    print(result)
