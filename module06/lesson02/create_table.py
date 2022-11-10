from psycopg2 import DatabaseError
from lesson02.connection import create_connection


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except DatabaseError as err:
        print(err)

if __name__ == '__main__':
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(120),
     email VARCHAR(120),
     password VARCHAR(120),
     age numeric CHECK (age > 10 AND age < 90)
    );"""

    with create_connection() as conn:
        if conn is not None:
            create_table(conn, sql_create_users_table)
        else:
            print('Error: can\'t create the database connection')