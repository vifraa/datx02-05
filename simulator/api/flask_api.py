from flask import Flask, jsonify,send_file, make_response, current_app
from flask_cors import CORS, cross_origin
import os
import sys

sys.path.insert(1, 'C:/Users/razan/Desktop/Kandidatarbetet/datx02-05/simulator')
print(os.path.abspath(os.getcwd()))

from generator import generate_individuals_with_param
from __init__ import train_population_from_file_random_program, train_population_from_file, train_population
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

with app.app_context():

    @app.route("/simulator")
    def index():
        return 'Hello from Simulator!'


    @app.route("/simulator/individuals/<n>/<bpm>/<bpv>")
    def individuals(n, bpm, bpv):
        try:
            os.remove('simulator/api/individuals/GeneratedIndividuals.csv')
            os.remove('models/api/individuals/GeneratedIndividuals.csv')
            print("Existing GeneratedIndividuals has been deleted")
        except FileNotFoundError:
            print("Nothing has been deleted")
        print("Debug here::::::: indidviduals")
        print(os.path.abspath(os.getcwd()))

        generate_individuals_with_param(int(n), int(bpm), int(bpv))

        print(os.path.abspath(os.getcwd()))

        dataframe = pd.read_csv('simulator/api/individuals/GeneratedIndividuals.csv', sep='|')

        data = dataframe.head()
        headers_list = dataframe.columns.values.tolist()
        data_to_send = data.values.tolist()
        data_to_send.insert(0, headers_list)

        #print(data_to_send)
        print("The population has been generated!")

        return jsonify(data_to_send)


    @app.route("/simulator/logs/<nr_train_before>/<nr_train_after>")
    def logs(nr_train_before, nr_train_after):
        print("Got the request!")
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
        random_pre_program = count == int(nr_train_before)
        no_pre_program = count + 1 == int(nr_train_before)
        training_program = programs_map_to_id[int(nr_train_after)]
        if not no_pre_program:
            if random_pre_program:
                train_population_from_file_random_program(
                    "simulator/api/individuals/GeneratedIndividuals.csv", programs_map_to_id,
                    "simulator/api/output/pre_program_logs.csv")
                train_population_from_file_random_program(
                    "simulator/api/individuals/GeneratedIndividuals.csv", programs_map_to_id,
                    "models/api/output/pre_program_logs.csv")
            else:
                pre_training_program = programs_map_to_id[int(nr_train_before)]
                train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                                           pre_training_program, "simulator/api/output/pre_program_logs.csv")
                train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                                           pre_training_program, "models/api/output/pre_program_logs.csv")
        train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                                   training_program, "simulator/api/output/program_logs.csv")
        train_population_from_file("simulator/api/individuals/GeneratedIndividuals.csv",
                                   training_program, "models/api/output/program_logs.csv")

        dataframe = pd.read_csv('simulator/api/output/program_logs.csv', sep='|')

        data = dataframe.head()
        headers_list = dataframe.columns.values.tolist()
        data_to_send = data.values.tolist()
        data_to_send.insert(0, headers_list)

        #print(data_to_send)
        print("The population has been trained!")

        return jsonify(data_to_send)



    @app.route("/simulator/generatedfiles")
    def generatedfiles_info():

        # Clean up past output
        generatedfiles_info = []
        Individuals_DIR = os.path.join("simulator", "api", "individuals")

        print("Debug here::           generatedfiles")
        print(os.path.abspath(os.getcwd()))

        for fn in os.listdir(Individuals_DIR):
            # Skip hidden files
            if fn.startswith('.'):
                continue
            print("printing here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(os.path.join(Individuals_DIR, fn))    
            data = pd.read_csv(os.path.join(Individuals_DIR, fn), sep="|")
            fdimentions = data.shape
            generatedfiles_info.append([fn, fdimentions])

        OUTPUT_DIR = os.path.join("simulator", "api", "output")
        for fn in os.listdir(OUTPUT_DIR):
            # Skip hidden files
            if fn.startswith('.') or fn == "pre_program_logs.csv":
                continue
            data = pd.read_csv(os.path.join(OUTPUT_DIR, fn), sep="|")
            fdimentions = str(data.shape)
            generatedfiles_info.append([fn, fdimentions])

        print("Debug finished::::: generated files")
        print(os.path.abspath(os.getcwd()))

        print(generatedfiles_info)
        return jsonify(generatedfiles_info)


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

        # individuals(10, 100, 5)
        # print(logs(1, 1))
        # generatedfiles_info()





