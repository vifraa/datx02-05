from flask import Flask, jsonify,send_file, make_response
from flask_cors import CORS, cross_origin
from generator import generate_individuals_with_param
import numpy as np
import csv

import sys
sys.path.append('../')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def index():
    return 'Hello world!'


@app.route("/individuals/<n>/<bpm>/<bpv>/<am>/<av>/<gr>/<wm>/<wv>")
def individuals(n, bpm, bpv, am, av, gr, wm, wv):
    import os
    try:
        os.chdir("../../")
        os.remove('simulator/api/individuals/GeneratedIndividuals.csv')
        print("Existing GeneratedIndividuals has been deleted")
    except FileNotFoundError:
        print("Nothing has been deleted")
    try:
        os.chdir("simulator/api")
        generate_individuals_with_param(n, bpm, bpv, am, av, gr, wm, wv)
        with open('simulator/api/individuals/GeneratedIndividuals.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        data = np.array(data)[0:6, :]
        return data
    except:
        return "The population couldn't be generated."


@app.route("/logs")
def logs(logs):
    return 2


@app.route("/<something>")
def something_(something):
    return 3


if __name__ == "__main__":
    import pathlib
    print(pathlib.Path().absolute())
    try:
        import os
        os.chdir("../../")
        os.remove('simulator/api/individuals/GeneratedIndividuals.csv')
        print("Existing GeneratedIndividuals has been deleted")
    except FileNotFoundError:
        print("Nothing has been deleted")
    os.chdir("simulator/api")
    generate_individuals_with_param(6, 100, 5, 30, 5, 0.5, 50, 5)
    with open('simulator/api/individuals/GeneratedIndividuals.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = np.array(data)[0:5, :]
    print(data)
    app.run(debug=True)




