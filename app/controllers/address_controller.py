from http import HTTPStatus
from sqlite3 import IntegrityError
from dotenv import load_dotenv
from flask import current_app, request, jsonify

import os
import json
from app.controllers.states_controller import create_state


from app.models.address_models import Address
from app.configs.database import db
from app.models.state_models import States

load_dotenv()

attributes = json.loads(os.getenv("ATTRIBUTES_ADDRESS"))



def create_address(received_address):
    session = current_app.db.session()
   
    data = received_address
    
    state_name = data.pop("state")
    state_id = create_state(state_name)
    keys = ["id","street", "number", "district", "zip_code", "city", "reference", "state"]

    try:
        address = Address.query.filter_by(street= data["street"]).filter_by(number = data["number"]).filter_by(district=data["district"]).filter_by(zip_code = data["zip_code"]).filter_by(city = data["city"]).filter_by(state_id = state_id).filter_by(reference = data["reference"]).all() 

        
        if len(address)==0:
            try:
                new_address = Address(**data)
                new_address.state_id = state_id
                
                
            except TypeError:
                return {"error":"Type error bad request"}, HTTPStatus.BAD_REQUEST
    
            missing_keys=[]

            for attribute in attributes:
                if attribute not in data.keys():
                    missing_keys.append(attribute)
            if len(missing_keys)>0:
                return {"Error":f"Missing keys: {missing_keys}"}
    
            for attribute in data.values():
                if type(attribute) != str:
                    return {'Error': f'{attribute[0]} must be a string'}, HTTPStatus.BAD_REQUEST

            try:
                session.add(new_address)
                session.commit()
        
            except IntegrityError:
                return {"Error":"Address already exists"}, HTTPStatus.CONFLICT

            
            values = [new_address.address_id,new_address.street, new_address.number, new_address.district, new_address.zip_code, new_address.city, new_address.reference, state_name]

            response = dict(zip(keys, values))
            return response

    except:
        ...
    r = address[0]
    values = [r.address_id, r.street, r.number, r.district, r.zip_code, r.city, r.reference, state_name]
    response = dict(zip(keys, values))
    return response