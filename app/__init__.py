from flask import Flask
from app.configs import database, migrations
from app import routes
import os



def create_app():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)

    return app