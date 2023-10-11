import os
import motor.motor_asyncio


MONGODB_URL="mongodb://admin:secret@mongodb/db?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.college