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



async def get_exchange(currency_code: str):
    result = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date=01.12.2022')
    if result:
        rates = result.get("exchangeRate")
        exc, = list(filter(lambda element: element["currency"] == currency_code, rates))
        return f"{currency_code}: buy: {exc['purchaseRateNB']}, sale: {exc['saleRateNB']}. Date: {datetime.now().date()}"
    return "Failed to retrieve data"
