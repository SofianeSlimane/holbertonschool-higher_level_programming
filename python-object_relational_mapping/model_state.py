#!/usr/bin/python3
"""This module containes our Base class which serves as a base for
 defining tables Python Object, User class inherits from it and
has its own columned(attributes) defined in it."""
from sqlalchemy import Column, Integer, String
import sys
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State subclass"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
