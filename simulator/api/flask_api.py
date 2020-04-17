from flask import Flask, jsonify,send_file, make_response
from flask_cors import CORS, cross_origin
from generator import generate_individuals_with_param
from __init__ import train_population_from_file_random_program, train_population_from_file, train_population
import numpy as np
import csv
import sys
import os

sys.path.append('../')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def index():
    return 'Hello world!'


@app.route("/individuals/<n>/<bpm>/<bpv>/<am>/<av>/<gr>/<wm>/<wv>")
def individuals(n, bpm, bpv, am, av, gr, wm, wv):
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
        if n > 6:
            data = np.array(data)[0:6, :]
        else:
            data = np.array(data)[:, :]
        return data
    except:
        return "The population couldn't be generated."


@app.route("/logs/<nr_train_before>/<nr_train_after>")
def logs(nr_train_before, nr_train_after):
    os.chdir("../../")
    # Clean up past output
    OUTPUT_DIR = os.path.join("simulator", "api", "output")
    for fn in os.listdir(OUTPUT_DIR):
        # Skip hidden files
        if fn.startswith('.'):
            continue
        os.remove(os.path.join(OUTPUT_DIR, fn))

    """
        Allows the user to choose which program was trained before and which program to 'actually' train.
        """
    PROGRAMS_DIR = os.path.join("simulator", "training_programs")
    programs_map_to_id = {}
    count = 1
    for fn in os.listdir(PROGRAMS_DIR):
        programs_map_to_id[count] = os.path.join(PROGRAMS_DIR, fn)
        count += 1
    # If user selected last number, we choose random
    random_pre_program = count == nr_train_before
    no_pre_program = count + 1 == nr_train_before
    training_program = programs_map_to_id[nr_train_after]
    if not no_pre_program:
        if random_pre_program:
            train_population_from_file_random_program(
                "simulator/api/individuals/GeneratedIndividuals.csv", programs_map_to_id,
                "simulator/api/output/pre_program_logs.csv")
        else:
            pre_training_program = programs_map_to_id[nr_train_before]
            train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                                       pre_training_program, "simulator/api/output/pre_program_logs.csv")
    train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                               training_program, "simulator/api/output/program_logs.csv")

    with open('simulator/api/individuals/GeneratedIndividuals.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = np.array(data)[0:10, :]
    return data  # "Your individuals were trained, results can be found in the output folder."


if __name__ == "__main__":
    """
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
    logs(1, 1)
    """
    app.run(debug=True)




