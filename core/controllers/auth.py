'''
Created on Feb 10, 2023

@author: desarrollador
'''
from fastapi.routing import APIRouter
from core.services.auth import create_token
from fastapi.responses import JSONResponse
from core.schemas.schemas import UserSchema

auth_router = APIRouter()


@auth_router.post('/login', tags=['Auth'])
def login(user: UserSchema):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

