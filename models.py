from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    field1 = Column(Text, unique=False)
