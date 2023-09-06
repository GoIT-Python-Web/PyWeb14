import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://web14user:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.web14

parser = argparse.ArgumentParser(description='Cats APP')

parser.add_argument('--action', help='Command: create, find, update, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arguments = vars(arguments)

action = my_arguments.get('action')
name = my_arguments.get('name')
age = my_arguments.get('age')
features = my_arguments.get('features')
pk = my_arguments.get('id')


def create(name_, age_, features_):
    result = db.cats.insert_one({
        'name': name_,
        'age': age_,
        'features': features_,
    })
    return result


def find():
    return db.cats.find()


def update(pk_, name_, age_, features_):
    result = db.cats.update_one({"_id": ObjectId(pk_)}, {
        "$set": {
            'name': name_,
            'age': age_,
            'features': features_,
        }
    })
    return result


def remove(pk_):
    result = db.cats.delete_one({"_id": ObjectId(pk_)})
    return result


def main():
    match action:
        case 'create':
            result = create(name, age, features)
            print(result)
        case 'find':
            result = find()
            [print(cat) for cat in result]
        case 'update':
            result = update(pk, name, age, features)
            print(result)
        case 'remove':
            result = remove(pk)
            print(result)
        case _:
            print('Unknown command')


if __name__ == '__main__':
    main()
