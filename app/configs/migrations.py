from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    from app.models.users_models import Users
    from app.models.rental_cars_models import RentalCars
    from app.models.cars_models import Cars

    Migrate(
        app,
        app.db,
        compare_type=True
    )
