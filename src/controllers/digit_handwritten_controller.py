from flask import request
from flask_accepts import accepts, responds
from flask.wrappers import Response
from flask_restx import Resource

from src.services import DigitHandWrittenService
from src.parsers import upload_parser
from src.api import api


digit_handwritten = api.namespace(
    name='digit-handwritten',
    description='Digit recognition operations'
)

service = DigitHandWrittenService()


@digit_handwritten.route('/create-model')
class CreateModel(Resource):
    @staticmethod
    def get():
        return service.create_model()

    @staticmethod
    def post():
        return service.create_model()


@digit_handwritten.route('/evaluate')
class Evaluate(Resource):
    @staticmethod
    def get():
        return service.evaluate()

    @staticmethod
    def post():
        return service.evaluate()


@digit_handwritten.route('/predict')
@digit_handwritten.expect(upload_parser)
class Prediction(Resource):
    @staticmethod
    def post():
        args = upload_parser.parse_args()
        image_file = args['image']
        return service.predict(image_file)
