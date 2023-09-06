from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://web14user:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

db = client.web14

# db.cats.insert_many([
#     {
#         'name': 'Lama',
#         'age': 2,
#         'features': ['ходить в лоток', 'не дає себе гладити', 'сірий'],
#     },
#     {
#         'name': 'Liza',
#         'age': 4,
#         'features': ['ходить в лоток', 'дає себе гладити', 'білий'],
#     },
# ])

print(db.cats.find())

for cat in db.cats.find():
    print(cat)
