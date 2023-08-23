from repository import select

class Task:
    TABLE_NAME = 'tasks'
    def __init__(self, name: str, description: str, owner: int):
        self.name = name
        self.description = description
        self.owner = owner 

    def __repr__(self) -> str:
        return f"TODO: {self.name}, description {self.description}, Owner: {self.owner}"
    
    @classmethod
    def get_all_tasks_from_db(cls):
        tasks = list()
        for task_data in select(cls.TABLE_NAME):
            tasks.append(cls(name=task_data[1], description=task_data[2], owner=task_data[3]))
        return tasks

    @classmethod
    def get_user_tasks_from_db(cls, user_id:int):
        tasks = list()
        for task_data in select(cls.TABLE_NAME, condition=f" owner_id={user_id} "):
            tasks.append(cls(name=task_data[1], description=task_data[2], owner=task_data[3]))
        return tasks

    
class User:
    TABLE_NAME = 'users'
    def __init__(self, _id: int, name: str):
        self._id = _id
        self.name = name
    
    @classmethod
    def get_all_users_from_db(cls):
        users = list()
        for user_data in select(cls.TABLE_NAME):
            users.append(cls(_id=user_data[0],name=user_data[1]))
        return users

    def get_my_todo(self):
        tasks = Task.get_user_tasks_from_db(self._id)
        return(tasks)

    @classmethod
    def find_busiest(cls):
        import sqlite3
        with sqlite3.connect('todo.db') as con:
            cur = con.cursor()
            cur.execute("SELECT users.id, COUNT(tasks.id)  from users JOIN tasks ON users.id=tasks.owner_id GROUP BY users.id ORDER BY COUNT(tasks.id) DESC;")
            res = cur.fetchall()
            print(res)