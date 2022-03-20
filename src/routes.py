from src.controllers import handwritten


def register_routes(api):
    api.add_namespace(handwritten)
