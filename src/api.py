from flask_restx import Api


api = Api(
    version='1.0',
    title='Char Recognizer Flask API',
    description='API to recognize characters',
    prefix='/api'
)


def config_api(app) -> Api:
    api.init_app(app)
    return api
