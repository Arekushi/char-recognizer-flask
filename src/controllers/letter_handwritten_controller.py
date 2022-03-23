from flask import request
from flask_accepts import accepts, responds
from flask.wrappers import Response
from flask_restx import Resource

from src.services import LetterHandWrittenService
from src.parsers import upload_parser
from src.api import api


letter_handwritten = api.namespace(
    name='letter-handwritten',
    description='Letter recognition operations'
)

service = LetterHandWrittenService()


@letter_handwritten.route('/create-model')
class CreateModel(Resource):
    @staticmethod
    def get():
        return service.create_model()


@letter_handwritten.route('/evaluate')
class Evaluate(Resource):
    @staticmethod
    def get():
        return service.evaluate()


@letter_handwritten.route('/predict')
@letter_handwritten.expect(upload_parser)
class Prediction(Resource):
    @staticmethod
    def post():
        args = upload_parser.parse_args()
        image_file = args['image']
        return service.predict(image_file)
