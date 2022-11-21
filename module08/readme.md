# Введение в NoSQL базы данных

## Перше заняття

`pymongo_example` - приклади `PyMongo`. Завести і показати процесс створення акаунту на https://cloud.mongodb.com
підставити свої креди, показати приклади. Запустити приклад `test_connect.py`.

В прикладі `finish_main.py` показується "правильне" створення декораторів через `wraps` та 
дати поняття розуміння необхідності валідування вхідних даних. Починаємо з `start_main.py`

Приклади команд:

```bash
(module08-6Z-0SJgN-py3.10) py .\finish_main.py --action create --name Simon --age 4 --features "Вредний" "Ходить мимо лотка"
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}
```

```bash
py .\finish_main.py --action find                                                                
{'_id': ObjectId('637b40a5256b93d9e9dd83bd'), 'name': 'Simon', 'age': '4', 'features': ['Вредний', 'Ходить мимо лотка']}

```