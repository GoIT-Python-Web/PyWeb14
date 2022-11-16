"""
SQLAlchemy core
"""

from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=False)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('fullname', String)
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        print('Додати user')
        ins_user = users.insert().values(fullname='Anna Saifulina')
        print(str(ins_user))
        result_user = conn.execute(ins_user)

        user_select = select(users)
        result = conn.execute(user_select)
        for row in result:
            print(row)

        print('Додати address')
        ins_address = addresses.insert().values(email_address='anna@gmail.com', user_id=result_user.lastrowid)
        print(str(ins_address))
        conn.execute(ins_address)
        address_select = select(addresses)
        result = conn.execute(address_select)
        for row in result:
            print(row)

        print('Знайти address of user')
        address_select = select(addresses.c.email_address, users.c.fullname).join(users)
        print(str(address_select))
        result = conn.execute(address_select)
        for row in result:
            print(row)
