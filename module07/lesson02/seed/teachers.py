import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Верхня частина це щоб запустити та працювали тут імпорти. При запуску з PycCharm. Докладніше читати тут:
# https://stackoverflow.com/questions/16981921/relative-imports-in-python-3/16985066#16985066

from faker import Faker
from database.db import session
from database.models import Teacher

fake = Faker()


def create_teachers():
    for _ in range(1, 6):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-10y')
        )
        session.add(teacher)
    session.commit()


if __name__ == '__main__':
    create_teachers()
