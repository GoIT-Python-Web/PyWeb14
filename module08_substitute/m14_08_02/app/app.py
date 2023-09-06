import json
from datetime import datetime

import pika

from models import Task


credentials = pika.PlainCredentials('pglbwiuh', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, credentials=credentials,
                              virtual_host='pglbwiuh'))
channel = connection.channel()

channel.exchange_declare(exchange='task_service', exchange_type='direct')
channel.queue_declare(queue='task_campaing', durable=True)
channel.queue_bind(exchange='task_service', queue='task_campaing')


def main():
    for i in range(1000):
        task = Task(consumer="Nonname").save()

        channel.basic_publish(
            exchange='task_service',
            routing_key='task_campaing',
            body=str(task.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
    connection.close()


if __name__ == '__main__':
    main()
