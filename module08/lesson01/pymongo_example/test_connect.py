from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://webpractic::<password>@cluster0.smeju.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))
db = client.test

if __name__ == '__main__':
    db.cats.insert_many([
        {
            "name": 'Lama',
            "age": 2,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Liza',
            "age": 4,
            "features": ['ходить в лоток', 'дає себе гладити', 'білий'],
        },
    ])

    r = db.cats.find({})

    for c in r:
        print(c)
