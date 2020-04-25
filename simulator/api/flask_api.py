from flask import Flask, jsonify,send_file, make_response, current_app
from flask_cors import CORS, cross_origin
import os
import sys
sys.path.insert(1, 'C:/Users/razan/Desktop/Kandidatarbetet/datx02-05/simulator')
import io
import matplotlib.pyplot as plt

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

        generate_individuals_with_param(int(n), int(bpm), int(bpv))

        dataframe = pd.read_csv('simulator/api/individuals/GeneratedIndividuals.csv', sep='|')


        if dataframe.shape[0] > 20:
            data = dataframe.head(20)
        else:
            data = dataframe

        headers_list = dataframe.columns.values.tolist()
        data_to_send = data.values.tolist()
        data_to_send.insert(0, headers_list)

        print("The population has been generated!")

        data.plot()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        img = send_file(bytes_image,
                     attachment_filename='plot.png',
                     mimetype='image/png')

        return jsonify(data_to_send)


    @app.route("/simulator/individuals/img")
    def individuals_img():
        dataframe = pd.read_csv('simulator/api/individuals/GeneratedIndividuals.csv', sep='|')
        dataframe.plot()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        img = send_file(bytes_image,
                        attachment_filename='plot.png',
                        mimetype='image/png')
        return img


    @app.route("/simulator/logs/<nr_train_before>/<nr_train_after>")
    def logs(nr_train_before, nr_train_after):
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

        if dataframe.shape[0] > 20:
            data = dataframe.head(20)
        else:
            data = dataframe

        headers_list = dataframe.columns.values.tolist()
        data_to_send = data.values.tolist()
        data_to_send.insert(0, headers_list)

        print("The population has been trained!")

        return jsonify(data_to_send)



    @app.route("/simulator/generatedfiles")
    def generatedfiles_info():

        # Clean up past output
        generatedfiles_info = []
        Individuals_DIR = os.path.join("simulator", "api", "individuals")

        for fn in os.listdir(Individuals_DIR):
            # Skip hidden files
            if fn.startswith('.'):
                continue
            data = pd.read_csv(os.path.join(Individuals_DIR, fn), sep="|")
            fdimentions = data.shape
            generatedfiles_info.append([fn, fdimentions])

        OUTPUT_DIR = os.path.join("simulator", "api", "output")
        for fn in os.listdir(OUTPUT_DIR):
            # Skip hidden files
            if fn.startswith('.') or fn == "pre_program_logs.csv":
                continue
            data = pd.read_csv(os.path.join(OUTPUT_DIR, fn), sep="|")
            fdimentions = data.shape
            generatedfiles_info.append([fn, fdimentions])


        print(generatedfiles_info)
        return jsonify(generatedfiles_info)


    @app.route("/simulator/trainingsets")
    def trainingsets():

        # Clean up past output
        generatedfiles_info = []

        trainingsets_DIR = os.path.join("simulator", "api", "trainingsets")
        for fn in os.listdir(trainingsets_DIR):
            # Skip hidden files
            if fn.startswith('.'):
                continue
            data = pd.read_csv(os.path.join(trainingsets_DIR, fn), sep="|")
            fdimentions = data.shape
            generatedfiles_info.append([fn, fdimentions])

        print(generatedfiles_info)
        return jsonify(generatedfiles_info)


    @app.route("/simulator/ttr_transform/<selectedDataset>/<dataset_name>")
    def ttr_transform(selectedDataset, dataset_name):
        import sys
        sys.path.insert(1, 'C:/Users/razan/Desktop/Kandidatarbetet/datx02-05')

        from recengine.data_parser import ttrdata_from_csv_population_4_weeks
        import pandas as pd

        """
        pre_logs = pd.read_csv("simulator/api/output/pre_program_logs.csv", sep="|")
        post_logs = ttrdata_from_csv_population_4_weeks("simulator/api/output/"+selectedDataset)

        headers = ["load_week1", "max_week1", "load_week2", "max_week2", "load_week3", "max_week3", "load_week4",
                   "max_week4", "Performance"]
        new_data = pd.DataFrame(columns=headers)
        new_data = new_data.append(post_logs)

        # %%
        pre_logs_grouped_by_ID = {}
        for p_id, group in pre_logs.groupby('ID'):
            pre_logs_grouped_by_ID[str(p_id)] = group

        # Transform data
        for index, _ in post_logs.iterrows():
            new_data.at[index, 'Performance'] = pre_logs_grouped_by_ID.get(str(index))["Performance"].values[-1]
        """

        # Loads raw data and transforms.
        logs = pd.read_csv("simulator/api/output/program_logs.csv", sep="|")

        # Calculate TTR_DATA based on pre-logs.
        ttr_data = ttrdata_from_csv_population_4_weeks("simulator/api/output/pre_program_logs.csv")

        post_logs = {}
        for p_id, group in logs.groupby('ID'):
            post_logs[str(p_id)] = group

        headers = ["load_week1", "max_week1", "load_week2", "max_week2", "load_week3", "max_week3", "load_week4",
                   "max_week4", "Performance"]

        new_data = pd.DataFrame(columns=headers)

        for index, row in ttr_data.iterrows():
            p_id = row["id"]
            ttr = row.drop("id").values.tolist()

            postperformance = post_logs.get(p_id)["Performance"].values[-1]
            ttr.append(postperformance)

            new_data = new_data.append(pd.Series(ttr, index=new_data.columns), ignore_index=True)

        new_data.to_csv("models/api/trainingsets/"+dataset_name+".csv", index=False)
        new_data.to_csv("simulator/api/trainingsets/"+dataset_name+".csv", index=False)

        if new_data.shape[0] > 20:
            data = new_data.head(20)
        else:
            data = new_data

        headers_list = new_data.columns.values.tolist()
        data_to_send = data.values.tolist()
        data_to_send.insert(0, headers_list)

        return jsonify(data_to_send)


    @app.route("/simulator/ttr/img/<dataset_name>")
    def ttr_img(dataset_name):
        dataframe = pd.read_csv("models/api/trainingsets/"+dataset_name+".csv", sep=',')
        dataframe.plot()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        img = send_file(bytes_image,
                        attachment_filename='plot.png',
                        mimetype='image/png')
        return img

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
        app.run(host= '127.0.0.1', port=12345, debug=True)

        # individuals(10, 100, 5)
        # print(logs(1, 1))
        # generatedfiles_info()





