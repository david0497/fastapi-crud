'''
Created on Feb 8, 2023

@author: desarrollador
'''
from sqlalchemy import Column, Integer, String, Boolean

from core.app import Base


class EmployeeModel(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    status = Column(Boolean)
