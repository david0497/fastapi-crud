from core.app import app
from core.controllers.employees import employees_router
from core.controllers.auth import auth_router


def registry_endpoints():
    app.include_router(employees_router)
    app.include_router(auth_router)
