Тека `starter` тут знаходиться початковий набір html, css, js файлів. Сторінки вже підготовлені під роутер і переходу
між сторінками немає. Всі шляхи до файлів абсолютні, крім картинок. Це для перевірки, що веб-сервер працює нормально.

## Перше заняття

Тека `lesson01` - перше заняття. Що повинно отримати в результаті.
- `simple_app.py` - HTTP server Hello world!
- `app.js` - Простий HTTP, Віддача `html`, статики - `css`, `js`, favicon. Прийом `POST` запросу без обробки.

## Друге заняття

Тека `lesson02` - друге заняття. Що повинно отримати в результаті.

Додаємо обробку POST запросу. Функція `self.save_data_to_json(data)`. Дані кладемо в `data/data.json`

Приклад парсингу даних з байт-рядка

```python
import urllib.parse
import re

data = b'name=Krabat&email=krabatua%40gmail.com&text=%D0%A2%D0%B5%D1%81%D1%82+%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5'

# data_parse = urllib.parse.unquote(re.sub(r'\+', ' ', data.decode()))
data_parse = urllib.parse.unquote_plus(data.decode(), encoding='utf-8')

data_parse = data_parse.split('&')
data_parse = [el.split('=') for el in data_parse]
data_parse = {key: value for key, value in data_parse}

print(data_parse)
```

Додаємо шаблонізатор jinja2 и рендеремо шаблон `blog.html`. Дані для рендерингу в `data/blog.json`

Socket - приклад простого передавання даних по сокет. `server.py` и `client.py`. Вони відправляють повідомлення
друг другу по черзі.

