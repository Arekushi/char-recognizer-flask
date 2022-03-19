from flask import request
from flask_accepts import accepts, responds
from flask.wrappers import Response
from flask_restx import Namespace, Resource

recognizer = Namespace(
    'recognizer',
    description='Character recognition operations'
)


@recognizer.route('/')
class Recognizer(Resource):
    def get(self):
        return {
            'result': 'test'
        }
