# Введение в NoSQL базы данных

## Перше заняття

### Папка `pymongo_example`

Папка `pymongo_example` - приклади `PyMongo`. Завести і показати процесс створення акаунту на https://cloud.mongodb.com
підставити свої креди, показати приклади. Запустити приклад `test_connect.py`.

В прикладі `finish_main.py` показується "правильне" створення декораторів через `wraps` та 
дати поняття розуміння необхідності валідування вхідних даних &mdash; функція `validate`. Починаємо з `start_main.py`
приходимо до `finish_main.py`

Приклади команд CLI `finish_main.py`:

```bash
(module08-6Z-0SJgN-py3.10) py .\finish_main.py --action create --name Simon --age 4 --features "Вредний" "Ходить мимо лотка"
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}
```

```bash
py .\finish_main.py --action find                                                                
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}
```

<hr/>

### Папка `mongoengine_example`

Приклади з документації. Розглянуто повний CRUD. 
- `create_records.py`
- `get_records.py`
- `update_record.py`
- `delete_record.py`

<hr/>

### Папка `redis_example`

Трошки прикладів з Redis. Redis через docker контейнер

## Друге заняття

RabitMQ

- `01_simple` https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- `02_tasks` https://www.rabbitmq.com/tutorials/tutorial-two-python.html
- `03_pub_sub` https://www.rabbitmq.com/tutorials/tutorial-three-python.html

Celery

- `04_celery`

- Приклад з конспекту [https://textbook.edu.goit.global/python-web-textbook/docs/module-08/module-08-02/celery_04](https://textbook.edu.goit.global/python-web-textbook/docs/module-08/module-08-02/celery_04)
Запустити, показати.