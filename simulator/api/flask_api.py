from flask import Flask, jsonify,send_file, make_response
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def index():
    return 'Hello world!'


@app.route("/individuals")
def individuals():
    return jsonify(1)


@app.route("/logs")
def logs(logs):
    return 2


@app.route("/<something>")
def something_(something):
    return 3


if __name__ == "__main__":
    app.run(debug=True)
