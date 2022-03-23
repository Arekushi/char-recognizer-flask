from flask_restx import Api
from src.controllers import digit_handwritten, letter_handwritten


def register_routes(api: Api):
    api.add_namespace(digit_handwritten)
    api.add_namespace(letter_handwritten)
