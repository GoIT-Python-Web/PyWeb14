# ORM SQLAlchemy

> Не забути, що на цьому модулі треба докладно пояснити зв'язок багато-до-багатьох


## Перше заняття

Приклад роботи з SQLAlchemy core - `example_01.py`. Створити таблиці, послідовно показати та виконати операції
Приклад роботи з сесіями - `example_02.py`. Теж створити таблиці та показати створення даних і запрос.

Далі, **CLI** застосунок - **TODO**. БД Postgres - запускаємо через Docker. Конфігурація в `config.ini` пояснити за 
файл конфігурації.

`signup.py` - це створення користувача в БД.

> Примітка: модулі - тут зараз шляхи прописані для загальної структури тек. На занятті це ж буде тека lesson01, тому
> треба буде змінити шляхи.
 

Мета - показати всі операції **CRUD** на основі сесій

Команди виглядають так, наприклад створити задачу Test з описом 'Short text', для користувача `krab`:

```bash
py .\lesson01\main.py --action create --title Test --desc 'Short text' --login krab    
```

Користувача `krab` створюємо заздалегідь за допомогою `signup.py`. Через параметр `action` визначаємо вид операції, але
в залежності від контексту команди забираємо додаткові параметри
Мета, щоб зрозуміли, що кожен користувач бачить тільки своє. Їм простіше далі буде зрозуміти авторизацію.

## Друге заняття

Використовуємо Postgres.
Спочатку створюємо моделі `Teacher`, `Student` та модель для зв'язків багато-до-багатьох `TeacherStudent`.
Пояснити поля: `teachers` та `students`

> Поля `contacts` у моделі `Student` спочатку немає як і моделі `ContactPerson`

Після, за допомогою `alembic` створюємо міграції. Виконуємо скрипти з теки `seed`: `teachers.py`, `students.py` та
`relationship.py`

Потім виконуємо запити з файлу `main.py`
Запит 2 не оптимальний, пояснити чому.

Інші операції CRUD показати з файлу `crud.py`

Розкоментити модель `ContactPerson` та властивість `contacts` моделі `Student`. Виконати нову міграцію.

Виконати `seed/contact.py`, а потім запрос з файлу `main_contact.py`. Пояснюючи кожен крок.

Показати хуки

```python
@listens_for(Student, 'before_insert')
def generate_license(mapper, connect, target):
     target.new_first_name()
```

```python
class Student(Base):
	...

    def new_first_name(self):
        self.first_name = f"Mr.{self.first_name}"
        return self.first_name
```

Показати гібрідні (вірутальні) властивості

```python
    # Властівість для відображення (гибрідні, віртулаьні в інших мовах)
    @hybrid_property
    def fullname(self):
        return self.first_name + ' ' + self.last_name
```