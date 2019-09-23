from flask import Flask

from App.config import Config
from App.views import mn as main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(main)

    return app

