"""
Module contains functionality to recommend different training programs to different individuals.
"""
import glob
import pickle
import os

class RecommendationEngine:
    """
    RecommendationEngine
    """

    def __init__(self, model_type):
        dir_path = os.path.join(os.path.dirname(__file__), model_type)
        file_paths = glob.glob(dir_path + "/*.sav")

        models = []
        for path in file_paths:
            with open(path, "rb") as f:
                models.append(pickle.load(f))
        self.models = models



    def recommend_training(self, data):
        """
        Recommends the best training program for the given data based on the RecommendationEngine's
        loaded models.

        Returns the prediction result.

        :param data: The data to predict on
        """

        current_best = None
        for model in self.models:
            prediction = model.predict(data)

            if current_best is None or current_best < prediction:
                current_best = prediction

        return current_best
