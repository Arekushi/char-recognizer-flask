from src.controllers import digit_handwritten


def register_routes(api):
    api.add_namespace(digit_handwritten)
