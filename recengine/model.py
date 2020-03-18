"""
Module contains class representation of working with a
prediction model.
"""
import pickle

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
            self.name = os.path.basename(file.name)
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


    def __str__(self):
        return f"name: {self.name}, predictor_path: {self.predictor_path}, last_prediction: {self.last_prediction}"
