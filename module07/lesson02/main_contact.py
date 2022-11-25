import sys
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from datetime import datetime
from database.db import session
from database.models import Student, Teacher, ContactPerson

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти всіх студентів з вчителями joinedload('teachers')
2 -- Знайти всіх студентів з вчителями .join('teachers')
"""


def get_students():
    students = session.query(Student).options(joinedload('teachers'), joinedload('contacts')).all()
    for s in students:
        print(vars(s))
        print(s.fullname)
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")
        print(f"{[f'id: {c.id} first_name: {c.first_name}' for c in s.contacts]}")


def get_students_join():
    students = session.query(Student).join('teachers').join('contacts').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")
        print(f"{[f'id: {c.id} first_name: {c.first_name}' for c in s.contacts]}")


if __name__ == '__main__':
    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()
        match task:
            case 1:
                get_students()
            case 2:
                get_students_join()
            case _:
                print('Шо це таке?')

