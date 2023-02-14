import asyncio
import logging

import websockets


async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    print(reply)
    await websocket.send(reply)


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # run forever


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as err:
        print('Stop server')
