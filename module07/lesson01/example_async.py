"""
SQLAlchemy session
"""
import asyncio
import aiosqlite
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, selectinload
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine('sqlite+aiosqlite:///:memory:', echo=True)
AsyncDBSession = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)


'''
Як об'єкт, що зв'язує стан бази та опис бази, в Python коді виступає Base, саме цей клас відповідає за "магію" 
синхронізації таблиць у базі даних та їх опису в Python класах Person та Address.
'''

# Base.metadata.create_all(engine)
Base.metadata.bind = engine


async def init_models():
    """
    The init_models function creates all the tables in the database.
    It is called automatically when this module is imported.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_models()
    async with AsyncDBSession() as session:
        new_person = Person(fullname="Michail")
        session.add(new_person)
        '''Зверніть увагу, щоб зміни набули чинності, були записані до бази, обов'язково потрібно виконати commit.'''

        # session.commit()

        new_address = Address(post_code='36065', street_name='Mazepa', person=new_person)
        session.add(new_address)
        await session.commit()

        new_person = Person(fullname="Alex")
        session.add(new_person)
        '''Зверніть увагу, щоб зміни набули чинності, були записані до бази, обов'язково потрібно виконати commit.'''

        # session.commit()

        new_address = Address(post_code='36065', street_name='Europe', person=new_person)
        session.add(new_address)
        await session.commit()

        '''Щоб отримати дані з бази, можна скористатися методом query:'''
        print('Знайти користувача')
        person = await session.execute(select(Person))
        person = person.scalars().first()
        print(person.id, person.fullname)
        print('Знайти адреси з користувачами')
        addresses = await session.execute(select(Address).join(Person))
        addresses = addresses.scalars().all()
        for address in addresses:
            print(
                f"id: {address.id}, code: {address.post_code}, street: {address.street_name}, owner: {address.person.fullname}")

if __name__ == '__main__':

    asyncio.run(main())
