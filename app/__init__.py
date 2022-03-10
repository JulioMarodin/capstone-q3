from flask import Flask
from app.configs import database, migrations, email
from app import routes



def create_app():
    app = Flask(__name__)
    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)
    email.init_app(app)

    #gambiarrinha pra resolver o problema do heroku

    return app 