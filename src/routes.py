from flask_restx import Api
from src.controllers import digit_handwritten, letter_handwritten


namespaces = [
    digit_handwritten,
    letter_handwritten
]


def register_routes(api: Api):
    for namespace in namespaces:
        api.add_namespace(namespace)
