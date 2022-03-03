from dataclasses import dataclass

from sqlalchemy import Column, String

from app.configs.database import db

@dataclass
class Users(db.Model):
    cnh: str
    cpf: str
    name: str
    email: str
    phone: str
    categorie_cnh: str

    __tablename__ = 'tb_users'

    cnh = Column(String(11), primary_key=True)
    cpf = Column(String(11), unique=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    categorie_cnh = Column(String(2), nullable=False)
