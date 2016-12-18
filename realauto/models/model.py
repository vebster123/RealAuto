from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date,
    Time,
    ForeignKey,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://fix213p.dsmynas.com/real_auto')
Session = sessionmaker()
Base = declarative_base(bind=engine)


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    concern = Column(Text, nullable=False)
    model = Column(Text, nullable=False)
    car_adverts = Column(Integer, ForeignKey("caradvert.id"))
    part_adverts = Column(Integer, ForeignKey("partadvert.id"))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)


phone = Column(Text, nullable=False)
name = Column(Text, nullable=False)
surname = Column(Text, nullable=False)
car_arverts = Column(Integer, ForeignKey("caradvert.id"))


class CarAdvert(Base):
    __tablename__ = 'caradvert'
    id = Column(Integer, primary_key=True)


user_id = Column(Integer, ForeignKey("user.id"))
car_id = Column(Integer, ForeignKey("car.id"))
text = Column(Text)
cost = Column(Integer, nullable=False)
defect_car_arverts = Column(Integer, ForeignKey("defectcaradvert.id"))
pictures = Column(Integer, ForeignKey("pictures.id"))


class DefectCarAdvert(Base):
    __tablename__ = 'defectcaradvert'
    id = Column(Integer, primary_key=True)
    car_advert_id = Column(Integer, ForeignKey("caradvert.id"))
    type_part_id = Column(Integer, ForeignKey("typepart.id"))


class TypePart(Base):
    __tablename__ = 'typepart'
    id = Column(Integer, primary_key=True)
    type = Column(Text, nullable=False)


part = Column(Text, nullable=False)
part_adverts = Column(Integer, ForeignKey("partadvert.id"))
defect_car_adverts = Column(Integer, ForeignKey("defectcaradvert.id"))


class PartAdvert(Base):
    __tablename__ = 'partadvert'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class Picture(Base):
    __tablename__ = 'partsType'
    id = Column(Integer, primary_key=True)
    link = Column(Text, nullable=False)


car_advert_id = Column(Integer, ForeignKey("caradvert.id"))
