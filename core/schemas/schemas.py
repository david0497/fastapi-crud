'''
Created on Feb 9, 2023

@author: desarrollador
'''
from pydantic import Field, BaseModel
from typing import Optional


class EmployeeSchema(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=15)
    lastname: str = Field(max_length=50)
    status: bool

    
class UserSchema(BaseModel):
    email:str
    password:str
