#REDIS:

start a redis instance
$ docker run --name some-redis -d redis

Access the container's shell:s
$ docker exec -it some-redis sh

$ redis-cli

### Redis CLI 
1. **Connecting to Redis**
   - Connect to a Redis server:
     ```bash
     redis-cli
     ```
   - Connect to a specific host and port:
     ```bash
     redis-cli -h host -p port
     ```
   - Connect with authentication:
     ```bash
     redis-cli -a password
     ```

2. **Basic Key Operations**
   - Set a key:
     ```bash
     SET key value
     ```
   - Get a key's value:
     ```bash
     GET key
     ```
   - Delete a key:
     ```bash
     DEL key
     ```
   - Check if a key exists:
     ```bash
     EXISTS key
     ```
   - Expire a key after a given number of seconds:
     ```bash
     EXPIRE key seconds
     ```
   - Get all keys matching a pattern:
     ```bash
     KEYS pattern
     ```

3. **String Operations**
   - Increment a number stored at a key:
     ```bash
     INCR key
     ```
   - Increment a number stored at a key by a specific amount:
     ```bash
     INCRBY key increment
     ```

4. **List Operations**
   - Push a value to the head of a list:
     ```bash
     LPUSH list value
     ```
   - Push a value to the tail of a list:
     ```bash
     RPUSH list value
     ```
   - Pop a value from the head of a list:
     ```bash
     LPOP list
     ```
   - Pop a value from the tail of a list:
     ```bash
     RPOP list
     ```
   - Get a range of elements from a list:
     ```bash
     LRANGE list start stop
     ```

5. **Set Operations**
   - Add one or more members to a set:
     ```bash
     SADD set member [member ...]
     ```
   - Remove one or more members from a set:
     ```bash
     SREM set member [member ...]
     ```
   - Get all members of a set:
     ```bash
     SMEMBERS set
     ```
   - Check if a member is in a set:
     ```bash
     SISMEMBER set member
     ```

6. **Hash Operations**
   - Set the string value of a hash field:
     ```bash
     HSET hash field value
     ```
   - Get the value of a hash field:
     ```bash
     HGET hash field
     ```
   - Get all fields and values in a hash:
     ```bash
     HGETALL hash
     ```
   - Delete one or more hash fields:
     ```bash
     HDEL hash field [field ...]
     ```

7. **Publish/Subscribe**
   - Subscribe to a channel:
     ```bash
     SUBSCRIBE channel
     ```
   - Publish a message to a channel:
     ```bash
     PUBLISH channel message
     ```

8. **Transaction**
   - Start a transaction:
     ```bash
     MULTI
     ```
   - Execute all commands issued after MULTI:
     ```bash
     EXEC
     ```
   - Discard all commands issued after MULTI:
     ```bash
     DISCARD
     ```


# RABBIT MQ

### RabbitMQ Docker Cheat Sheet

#### Setting Up RabbitMQ with Docker

1. **Pull the RabbitMQ Image**:
   ```bash
   docker pull rabbitmq:3-management
   ```
   - This command pulls the RabbitMQ image with the management plugin.

2. **Run RabbitMQ Container**:
   ```bash
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```
   - `-d` runs the container in detached mode.
   - `--name` assigns the container a name.
   - `-p 5672:5672` maps the default RabbitMQ port.
   - `-p 15672:15672` maps the management UI port.
   - `rabbitmq:3-management` specifies the image to use.

3. **Access RabbitMQ Management UI**:
   - Open a web browser and navigate to `http://localhost:15672/`.
   - Default login credentials are `username: guest` and `password: guest`.

#### Basic RabbitMQ Commands via Docker

4. **Accessing RabbitMQ CLI**:
   - To run RabbitMQ CLI commands, you need to exec into the container:
     ```bash
     docker exec -it rabbitmq bash
     ```
   - Inside the container, you can use `rabbitmqctl` to manage RabbitMQ.

5. **Listing Queues**:
   ```bash
   rabbitmqctl list_queues
   ```

6. **Listing Exchanges**:
   ```bash
   rabbitmqctl list_exchanges
   ```

7. **Listing Connections**:
   ```bash
   rabbitmqctl list_connections
   ```

#### Python Client for RabbitMQ

To interact with RabbitMQ from Python, you can use `pika`, a RabbitMQ client library.

8. **Install Pika**:
   ```bash
   pip install pika
   ```

9. **Basic Python Producer Example**:
   ```python
   import pika

   connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
   channel = connection.channel()

   channel.queue_declare(queue='hello')
   channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

   connection.close()
   ```

10. **Basic Python Consumer Example**:
    ```python
    import pika

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    ```

### Additional Notes

- Ensure Docker is installed and running on your machine before executing Docker commands.
- The management plugin in RabbitMQ provides a user-friendly interface to monitor and manage queues, exchanges, bindings, and more.
- The `pika` examples above are basic; for more complex operations, refer to the `pika` documentation.
- RabbitMQ and `pika` offer a wide range of messaging features like message acknowledgments, durable queues, exchanges, routing keys, etc., which are beyond the scope of this basic cheat sheet.


# Celery with Redis Backend Cheat Sheet

#### Initial Setup

1. **Install Celery and Redis (as a broker)**:
   ```bash
   pip install celery[redis]
   ```

2. **Set Up a Basic Celery App**:
   - Create a file named `celery.py` in your main project directory.
   - Define the Celery application instance:
     ```python
     from celery import Celery

     app = Celery('myapp', broker='redis://localhost:6379/0')
     app.conf.result_backend = 'redis://localhost:6379/0'
     ```

3. **Create a Task**:
   - In any module, define a task. For example, in `tasks.py`:
     ```python
     from .celery import app

     @app.task
     def add(x, y):
         return x + y
     ```

#### Running Celery

4. **Start Celery Worker**:
   - In the terminal, navigate to your project directory.
   - Run the worker with:
     ```bash
     celery -A myapp worker --loglevel=info
     ```
   - Replace `myapp` with the name of your Celery app.

5. **Call a Task Asynchronously**:
   - From your Python script, you can call the task:
     ```python
     from tasks import add
     result = add.delay(4, 4)
     ```

6. **Get the Result of a Task**:
   - To get the result of the task:
     ```python
     print(result.get(timeout=1))
     ```

#### Advanced Configuration

7. **Configuring Celery**:
   - You can configure Celery in the `celery.py` file:
     ```python
     app.conf.update(
         task_serializer='json',
         accept_content=['json'],
         result_serializer='json',
         timezone='Europe/London',
         enable_utc=True,
     )
     ```

8. **Periodic Tasks**:
   - To set up periodic tasks, use Celery beat:
     - Add a schedule to your Celery app config:
       ```python
       from datetime import timedelta

       app.conf.beat_schedule = {
           'add-every-30-seconds': {
               'task': 'tasks.add',
               'schedule': timedelta(seconds=30),
               'args': (16, 16)
           },
       }
       ```
     - Start Celery beat along with the worker:
       ```bash
       celery -A myapp beat --loglevel=info
       ```


### Additional Notes

- Ensure Redis is running as your Celery broker.
- The Celery worker should be running in the background or a separate terminal to process tasks.
- Celery tasks are defined as functions decorated with `@app.task`.
- Celery provides many more options for task routing, error handling, task prioritization, etc., which are beyond the scope of this basic cheat sheet.

This cheat sheet should help you get started with basic Celery operations. For more advanced configurations and use cases, refer to the official Celery documentation.
