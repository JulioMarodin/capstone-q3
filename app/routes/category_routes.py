from flask import Blueprint

from app.controllers.category_car_controller import create_category_car

bp = Blueprint("category", __name__, url_prefix="/categories")

bp.post("")(create_category_car)