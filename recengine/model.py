"""
Module contains class representation of a Model to be used for prediction.
"""
import pickle

class Model:
    """The Model class represents an machine learning model that can be 
    used for predicting training performance."""

    def __init__(self, model_path):
        """
        :param model_path: The full filepath for the model file.
        """

        if model_path is not None:
            self.model = pickle.loads(model_path)


    def predict(self, data):
        """Predict the data on the internal model."""
        return self.predict(data)
