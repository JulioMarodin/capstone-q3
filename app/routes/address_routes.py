from flask import Blueprint

from app.controllers import address_controller

bp = Blueprint("address", __name__, url_prefix="/address")

bp.post("")(address_controller.create_address)
bp.get("")(address_controller.get_address)