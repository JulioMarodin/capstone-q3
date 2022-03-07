from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from datetime import date

from app.configs.database import db


@dataclass
class Cars(db.Model):
    chassi: str
    license_plate: str
    brand: str
    model: str
    year: str
    color_car: str
    image: str
    current_km: float
    licensing_expiration: date
    daily_rental_price: float
    daily_fixed_km: int
    available: bool

    __tablename__ = 'tb_cars'

    chassi = Column(String, primary_key=True)
    license_plate = Column(String, unique=True, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(String, nullable=False)
    color_car = Column(String, nullable=False)
    image = Column(String, nullable=False)
    current_km = Column(Float, nullable=False)
    licensing_expiration = Column(DateTime, nullable=False)
    daily_rental_price = Column(Float, nullable=False)
    daily_fixed_km = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

    category_id = Column(Integer, ForeignKey('tb_category_car.category_id'), nullable=False)
    maintenance_id = Column(Integer, ForeignKey('tb_maintenance_car.maintenance_id'),nullable=True)