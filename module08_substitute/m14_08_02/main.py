import redis
import pickle


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = redis.Redis(host='localhost', port=6379, password=None)
    client.set("username", "Oleksandr")
    client.expire("username", 600)
    client.set("age", 22)
    client.expire("age", 600)

    username = client.get("username")
    age = client.get("age")
    print(username, age)

    client.set("data", pickle.dumps([1, 2, 3, 4]))
    data = client.get("data")
    print(pickle.loads(data))
    client.close()
