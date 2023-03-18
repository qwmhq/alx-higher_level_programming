#!/usr/bin/python3
"""model_state
ORM for class state"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'

    id = Column(Integer,
                autoincrement='auto',
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
