from dataclasses import dataclass
from sqlalchemy import Column, String, Float, DateTime
from datetime import date

from app.configs.database import db

@dataclass
class Maintenance(db.Model):
    maintenance_id : str
    last_maintenance : date
    next_maintenance : date
    repaired_items : str
    maintenance_price : float

    __tablename__ = 'tb_maintenance_car'

    maintenance_id = Column(String, primary_key=True)
    last_maintenance = Column(DateTime, nullable=False)
    next_maintenance = Column(DateTime, nullable=False)
    repaired_items = Column(String, nullable=False)
    maintenance_price = Column(Float, nullable=False)

