import os

from fastapi import FastAPI, Request, HTTPException
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi.security.http import HTTPBearer
from core.services.auth import validate_token

# fastAPI instance
app = FastAPI()
app.title = "FastAPI app"
app.version = "0.1"


class JWTBearer(HTTPBearer):

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")

        
# config database
sqlite_file_name = "database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
engine = create_engine(database_url, echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()
