from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello!</h1>"


FLASK_RUN_HOST = '0.0.0.0'
FLASK_RUN_PORT = 9797

http_server = WSGIServer((str(FLASK_RUN_HOST), int(FLASK_RUN_PORT)), app)
http_server.serve_forever()
