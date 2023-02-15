'''
Created on Feb 9, 2023

@author: desarrollador
'''
from core.app import app, Base, engine
from core.controllers import registry_endpoints

registry_endpoints()

# create tables database
Base.metadata.create_all(bind=engine)

if __name__ == 'main':
    app(host='0.0.0.0', port=5000, debug=True)

