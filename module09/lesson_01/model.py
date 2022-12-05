from datetime import datetime

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_url = Column(String(250), nullable=False)
    rating = Column(Integer, nullable=False)
    title = Column(String(150), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    created = Column(DateTime, default=datetime.now())

