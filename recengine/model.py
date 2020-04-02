"""
Module contains class representation of working with a
prediction model.
"""
import pickle
import os

class Model:
    """
    Model contains functionality for working with generated
    prediction models.
    """

    def __init__(self, predictor_path):
        """
        Creates a new Model, loading the prediction model from
        the given filepath.

        :param predictor_path: The path to the prediction model.
        """
        with open(predictor_path, "rb") as file:
            self.predictor = pickle.load(file)
            self.name = os.path.splitext(os.path.basename(file.name))[0]
            self.predictor_path = predictor_path
            self.last_prediction = None

    def predict(self, data):
        """
        Predicts what outcome the given data will have
        with the internal prediction model.

        :param data: The data to make a prediction on.
        """
        prediction = self.predictor.predict(data)
        self.last_prediction = prediction
        return prediction
