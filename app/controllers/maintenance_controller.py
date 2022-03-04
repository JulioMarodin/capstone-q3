from app.exception.missing_key import MissingKeyError
from app.exception.invalid_date import InvalidDateError

from app.services.error_treatment import filter_keys, missing_key, validate_date
from app.models.maintenance_car_models import Maintenance
from app.configs.database import db

from flask import request, jsonify

def create_maintenance():
    data = request.get_json()
    incoming_keys = data.keys()
    keys = Maintenance.keys
    
    try:
        last_maintenance = data["last_maintenance"]
        next_maintenance = data["next_maintenance"]
        filter_keys(incoming_keys, keys)
        missing_key(incoming_keys, keys)
        validate_date(last_maintenance, next_maintenance)

        maintenance = Maintenance(**data)

        db.session.add(maintenance)
        db.session.commit()

        return jsonify(maintenance), 201

    except KeyError as e:
        return e.args[0], 400

    except MissingKeyError as e: 
        return e.args[0], 400
    
    except InvalidDateError as e:
        return e.args[0], 400


def update_maintenance(id):
    data = request.get_json()
    incoming_keys = data.keys()
    keys = Maintenance.keys

    try:
        maintenance = Maintenance.query.get(id)

        for key, value in data.items():
            setattr(maintenance, key, value)

        last_maintenance = maintenance.last_maintenance
        next_maintenance = maintenance.next_maintenance
    
        filter_keys(incoming_keys, keys)
        validate_date(last_maintenance, next_maintenance)
        
        db.session.add(maintenance)
        db.session.commit()
        
        return jsonify(maintenance), 200
    
    except KeyError as e:
        return e.args[0], 400
    
    except InvalidDateError as e:
        return e.args[0], 400