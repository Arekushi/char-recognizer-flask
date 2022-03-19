from flask import Flask

from src.api import config_api
from src.config import configs


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(configs.get(config_name))

    config_api(app)

    return app
