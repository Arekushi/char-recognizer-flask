from flask import Flask

from src.api import config_api
from src.config import configs
from src.routes import register_routes


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(configs.get(config_name))

    api = config_api(app)
    register_routes(api)

    return app
