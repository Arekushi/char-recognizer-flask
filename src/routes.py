from src.controllers import recognizer


def register_routes(api):
    api.add_namespace(recognizer)
