# Модуль 9: Web-scraping

## Заняття 1: Beautiful Soup

`example_lecture_notes.py` и `model.py` - Приклад з конспекту

`wars_info` - збір втрат російської армії з сайту `https://index.minfin.com.ua/ua/russian-invading/casualties/`

## Заняття 2: Фреймворк Scrapy

Створюємо проект

```bash
scrapy startproject war_info
```

Створюємо двух павуків

Щоб знайти всі лінки

```bash
scrapy genspider get_links index.minfin.com.ua 
```

Щоб виконати збір даних

```bash
scrapy losses get_links index.minfin.com.ua 
```

Запуск збору лінків. Великий параметр `-O` перезаписуємо файл, маленький дописуємо. Також добавить в файл `settings.py`
наступний параметр `FEED_EXPORT_ENCODING = 'utf-8'`, щоб нормально записувалась укр мова.

```bash
scrapy crawl get_links -O links.json
```

Запуск збору даних. Там вже очікуємо, що лежить заповнений файл `links.json`

```bash
 scrapy crawl losses -O losses.json

```

Цей файл `losses.json` експортуємо в MongoDB хмарну базу з допомогою MongoDB Compass

Также можно через `pipelines.py` виконать вставку в БД.\

```python
from itemadapter import ItemAdapter


class WarInfoPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'date' in adapter.keys():
            print('-----------------------------------------')
            print(f'Можна виконать вставку в БД')
            print('-----------------------------------------')
        return item
```