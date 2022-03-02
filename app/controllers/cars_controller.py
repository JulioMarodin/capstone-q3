from dotenv import load_dotenv
from flask import current_app, request, jsonify
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


    exceptions_keys_data = ['current_km', 'daily_rental_price', 'daily_fixed_km']

    for attribute in data.items():

        if attribute[0] not in exceptions_keys_data:
            if type(attribute[1]) != str:
                return {'Error': f'{attribute[0]} must be a string'}, HTTPStatus.BAD_REQUEST
        else:
            if attribute[0] == 'daily_fixed_km':
                if type(attribute[1]) != int:
                    return {'Error': f'{attribute[0]} must be a int number'}, HTTPStatus.BAD_REQUEST
            else:
                if type(attribute[1]) != float:
                    return {'Error': f'{attribute[0]} must be a float number'}, HTTPStatus.BAD_REQUEST

    try:
        db.session.add(car)
        db.session.commit()
    except IntegrityError:
        return {'Error': 'chassi or license_plate already registered'}, HTTPStatus.CONFLICT

    
    return jsonify(car), HTTPStatus.CREATED
    


def get_all_cars():
    session: Session = db.session
    base_query = session.query(Cars)
    record_all_cars = base_query.all()

    if not record_all_cars:
        return {'Error': 'No data found'}, HTTPStatus.NOT_FOUND
    
    if not record_all_cars:
        return {'Error': f'Records not found'}, HTTPStatus.NOT_FOUND

    return jsonify(record_all_cars), HTTPStatus.OK


def update_car(chassi):
    data = request.get_json()

    if len(chassi) != 17:
            return {'Error': f'Chassis field must be 17 characters long'}, HTTPStatus.BAD_REQUEST


    car_update = Cars.query.get(chassi)

    print(car_update)

    if not car_update:
        return {'Error': f'Records not found'}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(car_update, key, value)


    current_app.db.session.add(car_update)
    current_app.db.session.commit()


    return "", HTTPStatus.NO_CONTENT


def remove_car(chassi):
    data = request.get_json()

    if len(chassi) != 17:
        return {'Error': f'Chassis field must be 17 characters long'}, HTTPStatus.BAD_REQUEST
    
    car_delete = Cars.query.filter_by(chassi=chassi)

    print('1', car_delete)
    print('2', car_delete.all())

    if len(car_delete.all()) == 0:
        return {'Error': f'Records not found'}, HTTPStatus.NOT_FOUND

    car_delete.delete()
    current_app.db.session.commit()

    return "", HTTPStatus.NO_CONTENT



def search_car(license_plate):

    license_plate_upper = license_plate.upper()

    cars_search = Cars.query.filter(Cars.license_plate.like(f'%{license_plate_upper}%'))

    car_search = cars_search.all()
    

    return jsonify(car_search), HTTPStatus.OK


    ...