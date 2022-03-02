from flask import Blueprint

from app.controllers import cars_controller


bp = Blueprint('cars', __name__, url_prefix='/cars')

bp.post('')(cars_controller.create_car)