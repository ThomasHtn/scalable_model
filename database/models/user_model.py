import os
import sys

from sqlalchemy import Column, Integer, String

from database.db_init import Base

# Add folder parent in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    workclass = Column(String)
    fnlwgt = Column(Integer)
    education = Column(String)
    education_num = Column(Integer)
    marital_status = Column(String)
    occupation = Column(String)
    relationship = Column(String)
    capital_gain = Column(Integer)
    capital_loss = Column(Integer)
    hours_per_week = Column(Integer)
    native_country = Column(String)
    income = Column(String)
