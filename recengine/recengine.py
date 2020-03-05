"""
Module contains functinality to recommend different training programs to different individuals.
"""
from simulator.individual import Individual

def recommend_training(individual: Individual, performance: float):
    """Based on an individual and its current performance, return the recommended training program
    and the estimated future performance.

    :param individual: The individual to recommend training program for.
    :param performance: The individuals current performance.
    """
    # TODO Refactor Individual/Create new one that contain performance within itself.
    # Unnessecary to treat it separat from the individual.

    models = load_models()

    current_best = None
    for model in models:
        prediction = predict_from_model(model, individual, performance)

        if current_best is None or current_best < prediction:
            current_best = prediction

    return current_best



def load_models():
    """Instantiates and returns the available models."""
    return []

def predict_from_model(model, individual: Individual, current_performance: float):
    """Predicts what performance an given individual would have after doing a training program
    from the given training model.

    :param model: The training model used for predicting.
    :param individual: The individual to predict post performance.
    :param current_performance: The current performace of the individual.
    """
    return 0
