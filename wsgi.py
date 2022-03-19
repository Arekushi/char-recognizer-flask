import os
from dotenv import load_dotenv
from src.app import create_app


load_dotenv()
app = create_app(os.getenv('FLASK_ENV', 'default'))


def run():
    app.run(port=5000, host='0.0.0.0')


if __name__ == '__main__':
    run()
