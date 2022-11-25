import sys
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from datetime import datetime
from database.db import session
from database.models import Student, Teacher

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти всіх студентів з вчителями joinedload('teachers')
2 -- Знайти всіх студентів з вчителями .join('teachers')
3 -- Знайти всіх вчителів зі студентами joinedload('students')
4 -- Знайти всіх вчителів зі студентами joinedload('students') фільтруємо час работи вчителів
"""


def get_students():
    students = session.query(Student).options(joinedload('teachers')).all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")


def get_students_join():
    students = session.query(Student).join('teachers').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload('students')).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {s.id} first_name: {s.first_name}' for s in t.students]}")


def get_teachers_filter():
    teachers = session.query(Teacher).options(joinedload('students')).filter(and_(
        Teacher.start_work > datetime(year=2015, month=1, day=1),
        Teacher.start_work < datetime(year=2021, month=1, day=1)
    )).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {s.id} first_name: {s.first_name}' for s in t.students]}")



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
            case 3:
                get_teachers()
            case 4:
                get_teachers_filter()
            case _:
                print('Шо це таке?')

