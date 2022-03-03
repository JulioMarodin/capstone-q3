from http import HTTPStatus
from sqlite3 import IntegrityError
from dotenv import load_dotenv
from flask import current_app, request, jsonify

import os
import json


from app.models.address_models import Address
from app.configs.database import db

load_dotenv()

attributes = json.loads(os.getenv("ATTRIBUTES_ADDRESS"))

def create_address():
    session = current_app.db.session()
    data = request.get_json()

    try:
        address = Address.query.filter_by(residence_street= data["residence_street"]).filter_by(residence_number = data["residence_number"]).filter_by(residence_district=data["residence_district"]).filter_by(residence_cep = data["residence_cep"]).filter_by(residence_city = data["residence_city"]).filter_by(residence_state = data["residence_state"]).filter_by(residence_reference = data["residence_reference"]).all() 

        if len(address)==0:
            try:
                new_address = Address(**data)
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
                return {"Error":"Adress already exists"}, HTTPStatus.CONFLICT

            return jsonify(new_address), HTTPStatus.CREATED

    except:
        ...
    return {"msg":"Address already exists"}, HTTPStatus.CONFLICT

  
    

def get_address():
    data = request.get_json()
    try:
        address = Address.query.filter_by(residence_street= data["residence_street"]).filter_by(residence_number = data["residence_number"]).filter_by(residence_district=data["residence_district"]).filter_by(residence_cep = data["residence_cep"]).filter_by(residence_city = data["residence_city"]).filter_by(residence_state = data["residence_state"]).filter_by(residence_reference = data["residence_reference"]).all() 
        if len(address)==0:
            address = create_address()
            return address
    except:
        ... 
    return jsonify(address), HTTPStatus.OK