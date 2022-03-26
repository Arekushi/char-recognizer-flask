from flask import Flask

from src.api import config_api
from src.cli import config_cli
from src.config import config_from_object
from src.routes import register_routes


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    config_from_object(app, config_name)
    config_cli(app)

    api = config_api(app)
    register_routes(api)

    return app
