from flask import Blueprint, Flask
from app.routes.users_route import bp as bp_users

from app.routes.cars_routes import bp as bp_cars

bp_api = Blueprint('api', __name__)

def init_app(app: Flask):
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_cars)

    app.register_blueprint(bp_api)