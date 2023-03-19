#!/usr/bin/python3
"""model_city
ORM for City class"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Base class"""
    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement='auto',
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
