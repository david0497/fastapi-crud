'''
Created on Feb 8, 2023

@author: desarrollador
'''
from typing import List
from core.services import employees
from fastapi.routing import APIRouter
from core.schemas.schemas import EmployeeSchema
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from core.app import JWTBearer
from fastapi import Depends

employees_router = APIRouter()


@employees_router.get("/employees", tags=['Employees'], response_model=List[EmployeeSchema], status_code=200, dependencies=[Depends(JWTBearer())])
def get_employees() -> List[EmployeeSchema]:
    return JSONResponse(status_code=200, content=jsonable_encoder(employees.get_employees()))


@employees_router.get("/employee/{employee_id}", tags=['Employees'], response_model=EmployeeSchema, status_code=200)
def get_one_employee(employee_id: str) -> EmployeeSchema:
    employee = employees.get_one_employee(employee_id)
    if not employee:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(employee))


@employees_router.post("/employee", tags=['Employees'], response_model=dict, status_code=201)
def registry_employe(employee: EmployeeSchema):
    return employees.create_employee(employee.dict())


@employees_router.put("/employee/{employee_id}", tags=['Employees'], response_model=List[EmployeeSchema], status_code=200)
def modify_employee(employee_id: str, employee: EmployeeSchema):
    return employees.update_employee(employee_id, employee)


@employees_router.delete("/employee/{employee_id}", tags=['Employees'], response_model=List[EmployeeSchema], status_code=200)
def remove_employee(employee_id: str):
    return employees.delete_employee(employee_id)
