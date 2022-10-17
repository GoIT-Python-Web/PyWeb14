from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://db:27017/")
db = client.web7


@app.route('/')
def index():
    result = {}
    cursor = db.users.find()
    for el in cursor:
        print(el)
        result.update({"id": str(el.get("_id")), "name": el.get("name")})
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0')
