from flask import Flask
from flask_migrate import Migrate

def init_app(app: Flask):
    from app.models.users_models import Users
    from app.models.rental_cars_models import RentalCars
    from app.models.cars_models import Cars
    from app.models.address_models import Address
    from app.models.state_models import States

    Migrate(
        app,
        app.db,
        compare_type=True
    )
