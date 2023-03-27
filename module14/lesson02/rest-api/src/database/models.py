import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, Enum
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.dialects.postgresql import ENUM as pgEnum

Base = declarative_base()


class Roles(enum.Enum):
    admin: str = "admin"
    moderator: str = "moderator"
    user: str = "user"


class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)


class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    age = Column(Integer)
    vaccinated = Column(Boolean, default=False)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=True)
    owner = relationship("Owner", backref="cats")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    roles = Column('role', Enum(Roles), default=Roles.user)
    confirmed = Column(Boolean, default=False)

#  CREATE TYPE roles AS ENUM ('admin', 'moderator', 'user'); for Postgres
