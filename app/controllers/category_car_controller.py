from app.services.error_treatment import filter_keys, missing_key
from app.models.categorie_car_model import Categorie_car
from app.exception.missing_key import MissingKeyError
from app.configs.database import db

from flask import request, jsonify

def create_category_car():
	data = request.get_json()
	incoming_keys = data.keys()
	keys = Categorie_car.keys
	
	try:
		filter_keys(incoming_keys, keys)
		missing_key(incoming_keys, keys)
		category_car = Categorie_car(**data)

		db.session.add(category_car)
		db.session.commit()

		return jsonify(category_car)
		
	except KeyError as e:
		return e.args[0], 400

	except MissingKeyError as e: 
		return e.args[0], 400
