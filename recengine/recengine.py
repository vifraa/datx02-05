"""
Module contains functionality to recommend different training programs to different individuals.
"""
import glob
import os
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
