from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    BIGINT,
    ForeignKey
)

Base = declarative_base()


class PartAdvert(Base):
    __tablename__ = 'part_advert'
    id = Column(BIGINT, primary_key=True)
    user_id = Column(BIGINT, ForeignKey('user.id'), nullable=False)
    car_id = Column(BIGINT, ForeignKey('car.id'), nullable=False)
    text = Column(Text, nullable=True)
    cost = Column(Integer, nullable=True)
