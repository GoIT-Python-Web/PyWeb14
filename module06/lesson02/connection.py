import psycopg2
from contextlib import contextmanager
from psycopg2 import Error


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='567234')
        yield conn
        conn.commit()
    except Error as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()
