# lesson01

Набор примеров для первого занятия папка `lesson01`. Можно их менять местами по дням. Так как из-за объема материала
асинхронная работа с файлами помещена во второй день:

- `01_intro.py` - базовый пример на `async/await`
- `02_fake_gather.py` - пример на использование `asyncio.gather`. Показывает сравнительное преимущество асинхронного
  подхода. Есть в конспекте.
- `03_fake_createtask.py` - Показываем `asyncio.create_task`, возможность создания нового Event loop, что под
  капотом `asyncio.run`
- `04_forever.py` - Пример замены `asyncio.run` на `loop.run_forever`
- `05_for_async_and_sync.py` - пример комбинирования синхронной и асинхронной функции. Скорость не больше длительности
  одной таски `get_user_async`.
- `06_for_await.py` - пример асинхронной функции в возвращающей список сопрограмм. Случай `for user in await users`
- `07_for_async.py` - пример асинхронного цикла. Случай `async for user in users:`
- `09_queue.py` - Пример использовании асинхронных очередей
- `10_global.py` и `11_context.py` - проблема глобальных переменных, для которых нужен контекст
- `12_blocking.py` - перевод блокирующих операций в неблокирующие
- `13_io_task.py` - ускоряем сетевые запросы `reqests`
- `14_cpu_task.py` - пример перевода синхронной функции, выполняющей тяжелые вычисления, в асинхронный формат

# lesson02

Набор примеров под второе занятие папка `lesson02`. 

- `01-03` - Примеры работы с Aiohttp client
- `task-runner` - Пример работы с пакетами `aiofile` и `aiopath`. Считываем файлы `js` из папки `files` и собираем их
в один файл `main.js`
- `sort-files` - пример асинхронной сортировки файлов. Пакеты  `aiopath` и `aioshutil`
Следующие три примера повторяют примеры из конспекта, можно рассмотреть если было не понятно и для закрепления материала
- `browser-ws` отправка сообщение из браузера на сервер и назад
- `consumer_producer` пример веб-сокет сервера с запоминанием клиента. Producer отправляет сообщение, consumer их слушает
- `chat` пример простого веб-чата. (Можно запустить локально и через ngrok пробросить тунель для общения)