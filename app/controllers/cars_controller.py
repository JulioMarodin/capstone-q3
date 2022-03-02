from dotenv import load_dotenv
from flask import request, jsonify
import os
import json
from http import HTTPStatus
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError

from app.models.cars_models import Cars
from app.configs.database import db


load_dotenv()

attributes = json.loads(os.getenv('ATTRIBUTES_CAR'))

def create_car():
    data = request.get_json()

    try:
        car = Cars(**data)
    except TypeError as e:
        return {'Error': 'Type error bad request'}, HTTPStatus.BAD_REQUEST

    missing_keys = []

    for attribute in attributes:
        if attribute not in data.keys():
            missing_keys.append(attribute)

    if len(missing_keys) > 0:
        return {'Error': f'Missing Keys: {missing_keys}'}, HTTPStatus.BAD_REQUEST


    exceptions_keys_data = ['current_km', 'daily_rental_price', 'daily_fixed_km' ]

    for attribute in data.items():

        if attribute[0] not in exceptions_keys_data:
            if type(attribute[1]) != str:
                return {'Error': f'{attribute[0]} must be a string'}, HTTPStatus.BAD_REQUEST
        else:
            if attribute[0] == 'daily_rental_price':
                if type(attribute[1]) != float:
                    return {'Error': f'{attribute[0]} must be a float number'}, HTTPStatus.BAD_REQUEST
            else:
                if type(attribute[1]) != int:
                    return {'Error': f'{attribute[0]} must be a int number'}, HTTPStatus.BAD_REQUEST

    try:
        db.session.add(car)
        db.session.commit()
    except IntegrityError:
        return {'Error': 'chassi or license_plate already registered'}, HTTPStatus.CONFLICT

    
    return jsonify(car), HTTPStatus.CREATED
    