from repository import init_db

from models import Task, User


init_db()

User.find_busiest()