import pika

import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

queue = channel.queue_declare(queue='', exclusive=True)
name_queue = queue.method.queue
channel.queue_bind(exchange='Events system', queue=name_queue)


def callback(ch, method, properties, body):
    message = json.loads(body.decode())
    print(f" [x] Received {message}")


channel.basic_consume(queue=name_queue, on_message_callback=callback, auto_ack=True)

if __name__ == '__main__':
    channel.start_consuming()
