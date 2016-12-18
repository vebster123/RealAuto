from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    BIGINT
)

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'
    id = Column(BIGINT, primary_key=True)
    concern = Column(Text, nullable=True)
    model = Column(Text, nullable=True)
