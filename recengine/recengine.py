"""
Module contains functionality to recommend different training programs to different individuals.
"""
import os
import glob
import pickle

def make_prediction(models, data):
    """Based on an individual and its current performance, return the recommended training program
    and the estimated future performance.

    :param individual: The individual to recommend training program for.
    :param performance: The individuals current performance.
    """

    current_best = None
    for model in models:
        prediction = model.predict(data)

        if current_best is None or current_best < prediction:
            current_best = prediction

    return current_best



def load_models(dir_path):
    """Instantiates and returns the available models at the directory path."""
    file_paths = glob.glob(dir_path + "/*.sav")

    models = []
    for path in file_paths:
        with open(path, "rb") as f:
            models.append(pickle.load(f))

    return models

