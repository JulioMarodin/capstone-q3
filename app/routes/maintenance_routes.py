from flask import Blueprint

from app.controllers.maintenance_controller import create_maintenance, get_maintenance_id, update_maintenance

bp = Blueprint("maintenance", __name__, url_prefix="/maintenance")

bp.post("")(create_maintenance)
bp.get("<id>")(get_maintenance_id)
bp.patch("<id>")(update_maintenance)