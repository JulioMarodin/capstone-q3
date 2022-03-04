from flask import request, jsonify, current_app
from dotenv import load_dotenv
from http import HTTPStatus
import os, json
from app.controllers.address_controller import create_address
from app.models.state_models import States


from app.models.users_models import Users

from app.configs.database import db

from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import NotFound

from app.models.users_models import Users

load_dotenv()

attributes = json.loads(os.getenv('ATTRIBUTES_USER'))

def create_user():

    data = request.get_json()

    address = data.pop("address")
    
    returned_address = create_address(address)
    try:
        user = Users(**data)
        user.id_address = returned_address["id"]
        
    except TypeError as e:
        return {'Error':'Type error'}, HTTPStatus.BAD_REQUEST

    missing_keys = []

    for attribute in attributes:
        if attribute not in data.keys():
            missing_keys.append(attribute)

    if len(missing_keys) > 0:
        return {'Error': f'Missing Keys: {missing_keys}'}, HTTPStatus.BAD_REQUEST

    for attribute in data.items():
        if type(attribute[0]) != str:
            return {'Error': f'{attribute[0]} must be a string'}, HTTPStatus.BAD_REQUEST
    
    try:
        
        print(user)
        db.session.add(user)
        db.session.commit()
        
       
    except IntegrityError:
        return {'Error': 'CPF or email already registered'}, HTTPStatus.CONFLICT
    

    return jsonify(user), HTTPStatus.CREATED


def get_users():
    users = Users.query.all()
    all_users = []
    for user in users:

        db_state = States.query.filter_by(state_id= user.user_address[0].state_id).one()
        user_address_keys = ["address_id", "street", "number", "district", "zip_code", "city", "reference", "state"]
        user_address_values = [user.user_address[0].address_id,user.user_address[0].street, user.user_address[0].number, user.user_address[0].district, user.user_address[0].zip_code, user.user_address[0].city, user.user_address[0].reference, db_state.name]

        user_address_response = dict(zip(user_address_keys, user_address_values))

        keys = ["cnh", "cpf", "name", "email", "phone", "categorie_cnh", "user_address"]
        values = [user.cnh, user.cpf, user.name, user.email, user.phone, user.categorie_cnh, user_address_response]
        response = dict(zip(keys, values))
        all_users.append(response)
    
        
    if not users:
        return {'error': 'users not found'}, HTTPStatus.NOT_FOUND

    return jsonify(all_users), HTTPStatus.OK


def patch_users(cnh):
    
    data = request.get_json()
    user = Users.query.get(cnh)

    for key, value in data.items():
        setattr(user, key, value)


    current_app.db.session.add(user)
    current_app.db.session.commit()

    data = {
        "email": user.email,
        "phone": user.phone,
        "categorie_cnh": user.categorie_cnh
    }

    return jsonify(data), HTTPStatus.OK


def delete_user(cnh):
    user = Users.query.get(cnh)

    try:
        current_app.db.session.delete(user)
        current_app.db.session.commit()
    except NotFound:
        return {'error': f'user cnh {cnh} not found'}, HTTPStatus.NOT_FOUND

    return {'message': f'user cnh {cnh} deleted'}, HTTPStatus.OK


def get_a_user(cnh):

    get_user = Users.query.get(cnh)

    try:

        db_state = States.query.filter_by(state_id= get_user.user_address[0].state_id).one()
        
        user_address_keys = ["address_id", "street", "number", "district", "zip_code", "city", "reference", "state"]
        user_address_values = [get_user.user_address[0].address_id,get_user.user_address[0].street, get_user.user_address[0].number, get_user.user_address[0].district, get_user.user_address[0].zip_code, get_user.user_address[0].city, get_user.user_address[0].reference, db_state.name]
        
        user_address_response = dict(zip(user_address_keys, user_address_values))
        
        print(get_user.cnh)

        keys = ["cnh", "cpf", "name", "email", "phone", "categorie_cnh", "user_address"]
        values = [get_user.cnh, get_user.cpf, get_user.name, get_user.email, get_user.phone, get_user.categorie_cnh, user_address_response]

        response = dict(zip(keys, values))
        print(response)


        return jsonify(response), HTTPStatus.OK
    except AttributeError:
        return {'error': f'user cnh {cnh} not found'}, HTTPStatus.NOT_FOUND
    
    