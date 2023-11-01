from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:root@localhost/flask", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class EmployeeModel(Base):
    __tablename__ = "employee"

    id = Column(Integer, Sequence('user_seq'), primary_key=True)
    name = Column(String(50), name='full_name', nullable=False)
    age = Column(Integer(3), nullable=False)
    position = Column(String(50), nullable=False)

    def __init__(self, name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.position}"
