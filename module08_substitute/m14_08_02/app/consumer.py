import pika

from models import Task


credentials = pika.PlainCredentials('pglbwiuh', 'password')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, credentials=credentials,
                              virtual_host='pglbwiuh'))
channel = connection.channel()

channel.queue_declare(queue='task_campaing', durable=True)


def callback(ch, method, properties, body):
    pk = body.decode()
    task = Task.objects(id=pk, completed=False).first()
    if task:
        task.update(set__completed=True, set__consumer="Krabaton")
        print(f"Task updated {task.id}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_campaing', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
