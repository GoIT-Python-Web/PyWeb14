import sys
import os
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Верхня частина це щоб запустити та працювали тут імпорти. При запуску з PycCharm. Докладніше читати тут:
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3/16985066#16985066

from faker import Faker
from database.db import session
from database.models import Student, ContactPerson

fake = Faker()


def create_contact_person():
    students = session.query(Student).all()

    for _ in range(len(list(students)) + 4):
        student = random.choice(students)
        cp = ContactPerson(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            student_id=student.id
        )
        session.add(cp)
    session.commit()


if __name__ == '__main__':
    create_contact_person()
