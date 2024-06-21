#!/usr/bin/python3
"""This module containes our Base class which serves as a base for
 defining tables Python Object, User class inherits from it and
has its own columned(attributes) defined in it."""
from sqlalchemy import Column, Integer, String, ForeignKey
import sys
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """State subclass"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
