#!/usr/bin/python3
"""
python file that contains the class definition of a City.
"""


import sqlalchemy
from sqlalchemy import Column, Integer, String ForeginKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """ Cities class

    Attributes:
            __tablename__: table to reference
            id: id of object instance
            name: string of max 128 chars not null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nulluble=False)
