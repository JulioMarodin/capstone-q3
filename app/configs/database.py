from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()


def init_app(app: Flask):

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    app.db = db


    db.create_all(app=app)
    app.db = db

    from app.models.users_models import Users
    from app.models.cars_models import Cars
    from app.models.address_models import Address
