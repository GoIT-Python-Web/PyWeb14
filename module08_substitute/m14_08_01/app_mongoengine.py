import argparse

from mongoengine import *

connect(
    db="web14",
    host="mongodb+srv://web14user:password@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
)


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


class Cat(Document):
    name = StringField(max_length=120, required=True)
    age = IntField(min_value=1, max_value=20)
    features = ListField(StringField(max_length=30))
    meta = {"collection": 'cats'}


def create(name_, age_, features_):
    cat = Cat(name=name_, age=age_, features=features_)
    cat.save()
    return cat


def find():
    return Cat.objects.all()


def update(pk_, name_, age_, features_):
    cat = Cat.objects(id=pk_).first()  # None is empty
    if cat:
        cat.update(name=name_, age=age_, features=features_)
        cat.reload()
    return cat


def update_v2(pk_, name_, age_, features_):
    try:
        cat = Cat.objects.get(id=pk_)
        cat.update(name=name_, age=age_, features=features_)
        cat.reload()
        return cat
    except DoesNotExist:
        return None


def remove(pk_):
    try:
        cat = Cat.objects.get(id=pk_)
        cat.delete()
        return cat
    except DoesNotExist:
        return None


def main():
    match action:
        case 'create':
            result = create(name, age, features)
            print(result.to_mongo().to_dict())
        case 'find':
            result = find()
            [print(cat.to_mongo().to_dict()) for cat in result]
        case 'update':
            result = update(pk, name, age, features)
            print(result.to_mongo().to_dict())
        case 'remove':
            result = remove(pk)
            print(result.to_mongo().to_dict())
        case _:
            print('Unknown command')


if __name__ == '__main__':
    main()
