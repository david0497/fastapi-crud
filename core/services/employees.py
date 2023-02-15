'''
Created on Feb 8, 2023

@author: desarrollador
'''
from core.models.models import EmployeeModel
from fastapi.responses import JSONResponse
from core.app import session

db = session()


def get_employees() -> list[EmployeeModel]:
    employees = db.query(EmployeeModel).all()
    return employees


def get_one_employee(employee_id: str) -> EmployeeModel:
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    return employee


def create_employee(data: dict) -> dict:
    new_employee = EmployeeModel(**data)
    db.add(new_employee)
    db.commit()
    return {'message': 'Registro éxitoso'}


def update_employee(employee_id:str, data: dict):
    employee = db.query(EmployeeModel).filter(id == employee_id).first()
    employee.name = data['name']
    employee.lastname = data['lastname']
    employee.status = data['status']
    employee.db.commit()
    return {'message': 'Actualizado con éxito'}


def delete_employee(employee_id:str) -> dict:
    employee = db.query(EmployeeModel).filter(id == employee_id).first()
    if not employee:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(employee)
    return {"message": "Se ha eliminado el empleado"}
