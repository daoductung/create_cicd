import gevent
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World 2!'


host = '0.0.0.0'
port = 9799
app_server = gevent.wsgi.WSGIServer((host, port), app)
app_server.serve_forever()
