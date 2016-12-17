from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    BIGINT
)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(BIGINT, primary_key=True)
    login = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    phone = Column(Integer, nullable=True)
    name = Column(Text, nullable=True)
    surname = Column(Text, nullable=True)
