from array import array
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import date

from app.configs.database import db

@dataclass
class Maintenance(db.Model):
    keys = ["last_maintenance", "next_maintenance", "repaired_items", "maintenance_price"]
    
    maintenance_id : Integer
    last_maintenance : date
    next_maintenance : date
    repaired_items : str
    maintenance_price : float

    __tablename__ = 'tb_maintenance_car'

    maintenance_id = Column(Integer, primary_key=True)
    last_maintenance = Column(DateTime, nullable=False)
    next_maintenance = Column(DateTime, nullable=False)
    repaired_items = Column(db.ARRAY(String), nullable=False)
    maintenance_price = Column(Float, nullable=False)

    @staticmethod
    def format_date(date):
        format = date.strftime("%d/%m/%Y")

        return format