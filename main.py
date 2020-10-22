from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello Tung Update!"


@app.route('/test')
def test():
    return "Update thanh cong r ne!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9799)
