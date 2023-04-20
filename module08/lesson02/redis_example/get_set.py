import redis


client = redis.StrictRedis(host="localhost", port=6379, password=None)

if __name__ == '__main__':
    client.set('foo', 'bar')
    client.set('baz', 100)

    print(client.get('foo').decode())
    print(int(client.get('baz').decode()))
