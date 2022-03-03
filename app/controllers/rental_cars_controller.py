from flask import request, jsonify, current_app
from dotenv import load_dotenv
from http import HTTPStatus
import os, json
from werkzeug.exceptions import NotFound

from app.models.rental_cars_models import RentalCars
from app.models.cars_models import Cars
from app.models.users_models import Users

def rent_car():
    try:
        load_dotenv()

        km_per_day = json.loads(os.getenv('KM_PER_DAY'))
        attributes = ['rental_date', 'rental_return_date', 'customer_cnh', 'car_license_plate']

        data = request.get_json()
        missing_keys = []

        for attribute in attributes:
            if attribute not in data:
                missing_keys.append(attribute)
        
        if len(missing_keys) > 0:
            return {'Error': f'Missing keys: {missing_keys}'}

        car_to_be_rented = Cars.query.filter_by(license_plate=data['car_license_plate']).first_or_404()
        is_cnh_in_database = Users.query.filter_by(cnh=data['customer_cnh']).first_or_404()
        rentals_not_returned = RentalCars.query.filter_by(customer_cnh=data['customer_cnh']).first()

        if rentals_not_returned:
            if rentals_not_returned.returned_car == False:
                return {'Error': 'User already rented a car and did not return it yet'}, HTTPStatus.CONFLICT

        if car_to_be_rented.available == False:
            return {'Error': 'Car already rented'}, HTTPStatus.CONFLICT

        plate = data.pop('car_license_plate')
        rental_info = {
            'returned_car': False,
            'initial_km': car_to_be_rented.current_km,
            'total_fixed_km': km_per_day,
            'rental_value': car_to_be_rented.daily_rental_price * data['rental_total_days'],
            'car_license_plate': plate.upper()
        }

        setattr(car_to_be_rented, 'available', False)
        current_app.db.session.add(car_to_be_rented)
        current_app.db.session.commit()
        
        rental_car = RentalCars(**data, **rental_info)

        current_app.db.session.add(rental_car)
        current_app.db.session.commit()

        return jsonify(rental_car)
    except NotFound:
        return {'Error': 'Car or cnh not found!'}, HTTPStatus.NOT_FOUND


def return_car():
    try:
        load_dotenv()

        km_per_day = json.loads(os.getenv('KM_PER_DAY'))
        km_after_limit = json.loads(os.getenv('PRICE_PER_KM_AFTER_LIMIT'))
        day_after_limit = json.loads(os.getenv('PRICE_PER_DAY_AFTER_LIMIT'))

        attributes = ['rental_real_return_date', 'rental_real_total_days', 'total_returned_km']

        data = request.get_json()
        missing_keys = []

        for attribute in attributes:
            if attribute not in data:
                missing_keys.append(attribute)

        if len(missing_keys) > 0:
            return {'Error': f'Missing keys: {missing_keys}'}
        
        car_to_be_returned = Cars.query.filter_by(license_plate=data['car_license_plate'].upper()).first_or_404()
        is_cnh_in_database = Users.query.filter_by(cnh=data['cnh']).first_or_404()
        rental_not_returned = RentalCars.query.filter_by(customer_cnh=data['cnh'],returned_car=False).first()

        if not rental_not_returned:
            return {'Error': 'User has no rental pending'}, HTTPStatus.BAD_REQUEST

        real_km_per_day = (data['total_returned_km'] - rental_not_returned.initial_km) / data['rental_real_total_days']

        to_pay_per_km = 0
        if real_km_per_day > km_per_day:
            to_pay_per_km = (real_km_per_day - km_per_day) * km_after_limit * data['rental_real_total_days']

        to_pay_per_day = 0
        if data['rental_real_total_days'] > rental_not_returned.rental_total_days:
            to_pay_per_day = (data['rental_real_total_days'] - rental_not_returned.rental_total_days) * day_after_limit
        
        user_info_to_be_patched = {
            'rental_real_return_date': data['rental_real_return_date'],
            'returned_car': True,
            'rental_real_total_days': data['rental_real_total_days'],
            'final_km': data['total_returned_km'] - rental_not_returned.initial_km,
            'total_returned_km': data['total_returned_km'],
            'rental_real_value': rental_not_returned.rental_value + to_pay_per_km + to_pay_per_day
        }

        for key, value in user_info_to_be_patched.items():
            setattr(rental_not_returned, key, value)
        
        setattr(car_to_be_returned, 'available', True)
        setattr(car_to_be_returned, 'current_km', data['total_returned_km'])

        current_app.db.session.add(rental_not_returned)
        current_app.db.session.add(car_to_be_returned)
        current_app.db.session.commit()

        return jsonify(rental_not_returned), HTTPStatus.OK


    except NotFound:
        return {'Error': 'Car or cnh not found'}, HTTPStatus.NOT_FOUND


def get_all():
    all_invoices = RentalCars.query.all()

    return jsonify(all_invoices), HTTPStatus.OK

def get_by_plate(plate):
    try:
        invoice = RentalCars.query.filter_by(car_license_plate=plate.upper(),returned_car=False).first_or_404()

        return jsonify(invoice), HTTPStatus.OK
    
    except NotFound:
        return {'Error': 'Car not found'}, HTTPStatus.NOT_FOUND

def get_all_by_users(cnh):
    invoice = RentalCars.query.filter_by(customer_cnh=cnh).all()

    if len(invoice) == 0:
        return {'Error': 'User not found or never rented a car'}, HTTPStatus.NOT_FOUND

    return jsonify(invoice), HTTPStatus.OK

def get_current_rental_by_user(cnh):
    try:
        invoice = RentalCars.query.filter_by(customer_cnh=cnh,returned_car=False).first_or_404()

        return jsonify(invoice), HTTPStatus.OK
    
    except NotFound:
        return {'Error': 'User not found or not renting any car'}, HTTPStatus.NOT_FOUND