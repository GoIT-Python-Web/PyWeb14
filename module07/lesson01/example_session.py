"""
SQLAlchemy session
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Mapped

engine = create_engine('sqlite:///:memory:', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


users_to_address = Table('users_to_address',Base.metadata, 
              Column('id', Integer, primary_key=True),
              Column('persons_id', Integer, ForeignKey('persons.id')),
              Column('address_id', Integer, ForeignKey('addresses.id'))
              )

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    # person_id = Column(Integer, ForeignKey('persons.id'))
    persons: Mapped[list[Person]] = relationship(Person, backref="address", secondary=users_to_address)


'''
Як об'єкт, що зв'язує стан бази та опис бази, в Python коді виступає Base, саме цей клас відповідає за "магію" 
синхронізації таблиць у базі даних та їх опису в Python класах Person та Address.
'''

Base.metadata.create_all(engine)
Base.metadata.bind = engine

if __name__ == '__main__':

    '''
    ORM підхід виразніший. Наприклад, додавання нових записів до таблиці – це просто створення нових об'єктів класів Person 
    та Address:
    '''

    new_person = Person(fullname="Michail")
    session.add(new_person)
    '''Зверніть увагу, щоб зміни набули чинності, були записані до бази, обов'язково потрібно виконати commit.'''

    # session.commit()

    new_address = Address(post_code='36065', street_name='Mazepa', persons=[new_person])
    session.add(new_address)
    session.commit()
    # print(new_address.persons[0].fullname)
    # print(new_person.address[0].street_name)
    '''Щоб отримати дані з бази, можна скористатися методом query:'''
    print('Знайти користувача')
    person = session.query(Person).one()
    print(person.id, person.fullname)
    print('Знайти адреси з користувачами')
    # addresses = session.query(Address).join(Address.person).all()
    addresses = session.query(Address).all()
    for address in addresses:
        print(
            f"id: {address.id}, code: {address.post_code}, street: {address.street_name}, owner: {address.persons[0].fullname}")
