from src.api import api
from werkzeug.datastructures import FileStorage


upload_parser = api.parser()
upload_parser.add_argument(
    'image',
    type=FileStorage,
    location='files',
    required=True
)
