from flask import request, jsonify, current_app
from dotenv import load_dotenv
from http import HTTPStatus
import os, json


from app.models.users_models import Users

from app.configs.database import db

from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import NotFound

from app.models.users_models import Users

load_dotenv()

attributes = json.loads(os.getenv('ATTRIBUTES_USER'))

def create_user():

    data = request.get_json()

    try:
        user = Users(**data)
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
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        return {'Error': 'CPF or email already registered'}, HTTPStatus.CONFLICT
    

    return jsonify(user), HTTPStatus.CREATED


def get_users():
    users = (Users.query.all())

    if not users:
        return {'error': 'users not found'}, HTTPStatus.NOT_FOUND

    return jsonify(users), HTTPStatus.OK


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

    if not get_user:
        return {'error': f'user cnh {cnh} not found'}, HTTPStatus.NOT_FOUND
    
    return jsonify(get_user), HTTPStatus.OK