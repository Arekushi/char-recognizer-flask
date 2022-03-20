from flask import request
from flask_accepts import accepts, responds
from flask.wrappers import Response
from flask_restx import Resource

from src.services import create_model_tf, evaluate_tf, predict_tf
from src.parsers import upload_parser
from src.api import api


handwritten = api.namespace(
    name='handwritten',
    description='Character recognition operations'
)


@handwritten.route('/create-model')
class CreateModel(Resource):
    @staticmethod
    def get():
        return create_model_tf()

    @staticmethod
    def post():
        return create_model_tf()


@handwritten.route('/evaluate')
class Evaluate(Resource):
    @staticmethod
    def get():
        return evaluate_tf()

    @staticmethod
    def post():
        return evaluate_tf()


@handwritten.route('/predict')
@handwritten.expect(upload_parser)
class Prediction(Resource):
    @staticmethod
    def post():
        args = upload_parser.parse_args()
        image_file = args['image']
        return predict_tf(image_file)
