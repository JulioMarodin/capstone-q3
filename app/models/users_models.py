from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.configs.database import db

@dataclass
class Users(db.Model):
    cnh: str
    cpf: str
    name: str
    email: str
    phone: str
    category_cnh: str

    id_address: int

    user_address: str

    __tablename__ = 'tb_users'

    cnh = Column(String(11), primary_key=True)
    cpf = Column(String(11), unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    category_cnh = Column(String(2), nullable=False)

    id_address = Column(Integer, ForeignKey("tb_address.address_id"), nullable=False)

    user_address = relationship("Address", back_populates="address", uselist=True)
