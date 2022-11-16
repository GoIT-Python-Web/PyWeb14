import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Верхня частина це щоб запустити та працювали тут імпорти. При запуску з PycCharm. Докладніше читати тут:
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3/16985066#16985066

import random
from faker import Faker
from database.db import session
from database.models import Teacher, Student, TeacherStudent

fake = Faker()


def create_relationship():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    for student in students:
        teacher = random.choice(teachers)
        rel = TeacherStudent(teacher_id=teacher.id, student_id=student.id)
        session.add(rel)
    session.commit()


if __name__ == '__main__':
    create_relationship()
