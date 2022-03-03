from flask import request, jsonify, current_app
from http import HTTPStatus
import os, json

from app.models.rental_cars_models import RentalCars

def rent_car():
    attributes = ['rental_date', 'rental_return', 'returned_car', 'rental_total_days', 'initial_km', 'total_fixed_km', 'rental_value', 'customer_cnh', 'car_license_plate']

    data = request.get_json()
    missing_keys = []

    for attribute in attributes:
        if attribute not in data:
            missing_keys.append(attribute)
    
    if len(missing_keys) > 0:
        return {'Error': f'Missing keys: {missing_keys}'}
    
    rental_car = RentalCars(**data)

    current_app.db.session.add(rent_car)
    current_app.db.session.commit()

    return jsonify(rental_car)