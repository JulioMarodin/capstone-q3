from flask import Blueprint, Flask
from app.routes.users_route import bp as bp_users
from app.routes.category_routes import bp as bp_category
from app.routes.cars_routes import bp as bp_cars
from app.routes.address_routes import bp as bp_address
from app.routes.maintenance_routes import bp as bp_maintenance

bp_api = Blueprint('api', __name__)

def init_app(app: Flask):

    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_cars)
    bp_api.register_blueprint(bp_category)
    bp_api.register_blueprint(bp_address)
    bp_api.register_blueprint(bp_maintenance)

    app.register_blueprint(bp_api) 