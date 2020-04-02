"""
Module contains functionality to recommend different training programs to different individuals.
"""
import glob
import os
from collections import defaultdict
import csv
from datetime import datetime
import json
from model import Model

class RecommendationEngine:
    """
    RecommendationEngine
    """

    def __init__(self, model_type):
        dir_path = os.path.join(os.path.dirname(__file__), model_type)
        file_paths = glob.glob(dir_path + "/*.sav")

        models = []
        for path in file_paths:
            models.append(Model(path))

        self.models = models



    def recommend_training(self, data):
        """
        Recommends the best training program for the given data based on the RecommendationEngine's
        loaded models.

        Return value 1: A map containing the value `predicted_performance` and the `model` used.
        Return value 2: A list containing all models with their prediction in the same format
        as return value 1.

        :param data: The data to predict on
        """

        predictions = [{"predicted_performance": model.predict(data)[0], "model": model}
                       for model in self.models]
        predictions = sorted(predictions, key=lambda x: -x["predicted_performance"])
        return predictions[0], predictions

class ProgramSet:
    """
    Class representation of a training set in a
    training program.
    """

    def __init__(self, row):
        self.exercise = int(row[0])
        self.percent_1rm = float(row[1])
        self.repetitions = int(row[2])
        self.date = datetime.strptime(row[3], "%m/%d/%Y %H:%M").date()
        self._str_date = row[3]
        self.rest = None

    def __dict__(self):
        return {
            "date": self._str_date,
            "rest": self.rest,
            "repetitions": self.repetitions,
            "exercise": self.exercise,
            "percent_1rm": self.percent_1rm
        }

    def toJSON(self):
        """
        Converts the object to a json string.
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def fetch_program_from_model(model):
    """
    Based on an inputted model fetches and returns the training program
    used to generate the data to create the model.

    :param model: The model to fetch the training program for.
    """
    predictor_name = os.path.basename(model.predictor_path)
    file_name = os.path.splitext(predictor_name)[0]+'.csv'

    program_folder_path = os.path.join(os.path.dirname(
        __file__), os.pardir, 'simulator', 'training_programs')
    program_path = os.path.join(program_folder_path, file_name)

    try:
        with open(program_path, newline='') as file:
            program_reader = csv.reader(file, delimiter="|")
            _headers = next(program_reader)

            program = defaultdict(list)
            previous_set = None
            current_day_index = 0
            for row in program_reader:
                pset = ProgramSet(row)

                if previous_set is None:
                    current_day_index += 1
                    program[str(current_day_index)].append(pset)

                elif previous_set.date == pset.date:
                    program[str(current_day_index)].append(pset)
                    previous_set = pset

                else:
                    current_day_index += 1
                    previous_set = pset
                    program[str(current_day_index)].append(pset)

                previous_set = pset

    except FileNotFoundError:
        return {}

    return program
