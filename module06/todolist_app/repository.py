import sqlite3

from faker import Faker 
import random

def create_db():
    with open('init_todo.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(sql)



def populate_db():
    users_sql_command = "\n".join(f"INSERT INTO users (name) VALUES ('{Faker().name()}');" for _ in range(10))
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(users_sql_command)
        cur.execute("SELECT id from users;")
        user_ids = [obj[0] for obj in cur.fetchall()]        
        print(user_ids)

    tasks_sql_command = "\n".join(f"INSERT INTO tasks (name, description, owner_id) VALUES ('to_do_{i}', 'do something', {random.choice(user_ids)});" for i in range(40) )

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.executescript(tasks_sql_command)





def check_db():
    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from users;")
        result = cur.fetchall()
    print(result)

    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from tasks;")
        result = cur.fetchall()
    print(result)


def select(table_name:str, condition=None):
    if condition is not None:
        querry = f"SELECT * FROM {table_name} WHERE {condition};"
    else:
        querry = f"SELECT * FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result

def delete(table_name:str, condition=None):
    if condition is not None:
        querry = f"DELETE  FROM {table_name} WHERE {condition};"
    else:
        querry = f"DELETE  FROM {table_name};"


    with sqlite3.connect('todo.db') as con:
        cur = con.cursor()
        cur.execute(querry)
        result = cur.fetchall()
    return result


def init_db():
    create_db()
    populate_db()



