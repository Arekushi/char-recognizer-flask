from flask_restx import Api

from src.routes import register_routes


api = Api(
    version='1.0',
    title='Char Recognizer Flask API',
    description='API to recognize characters',
    prefix='/api'
)


def config_api(app):
    api.init_app(app)
    register_routes(api)
