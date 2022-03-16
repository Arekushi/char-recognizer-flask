from flask import Flask
app = Flask(__name__)


@app.route('/ping')
def ping_pong():
    return {
        'result': 'pong'
    }


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
