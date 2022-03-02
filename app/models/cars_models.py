from dataclasses import dataclass
from xmlrpc.client import DateTime
from sqlalchemy import Column, Integer, String, Float, DateTime
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

    # ## 15 jan a 10 fev -> 176kwh

    # 0 - 30 = 0,95 * 30 = 28,50 * 0,35 = 9,975
    # 31 - 100 = 0,95 * 70 = 66,5 * 0,6 = 39,90
    # 101 - 220 = 0,95 * 76 = 72,20 * 0,9 = 64,98
    # 0,95 * 20 = 19 * 0,9 = 17,10
