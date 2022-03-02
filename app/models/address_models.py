from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from app.configs.database import db

@dataclass
class Address(db.Model):
    address_id: int
    residence_street: str
    residence_number: str
    residence_district: str
    residence_cep: str
    residence_city: str
    residence_state: str
    residence_reference: str

    __tablename__ = 'tb_address'

    address_id = Column(Integer, primary_key=True)
    residence_street = Column(String, nullable=False)
    residence_number = Column(String, nullable=False)
    residence_district = Column(String, nullable=False)
    residence_cep = Column(String(8), nullable=False)
    residence_city = Column(String, nullable=False)
    residence_state = Column(String, nullable=False)
    residence_reference = Column(String, nullable=False)  