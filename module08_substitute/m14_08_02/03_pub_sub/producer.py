import json
from datetime import datetime
from random import randint
from time import sleep

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='Events system', exchange_type='fanout')



def main():
    message = {
        "event number": randint(1, 10),
        "detail": datetime.now().isoformat()
    }

    channel.basic_publish(
        exchange='Events system',
        routing_key='',
        body=json.dumps(message).encode(), )
    print(" [x] Sent %r" % message)


    connection.close()

if __name__ == '__main__':
    main()
