import pandas as pd
from individual import Individual
from generator import load_individuals


def infer_model_parameters(individuals_path, training_protocol_path, expected_results):
    """Run training study in accordance to given population parameters, training protocols and
    expected results. The internal modelling parameters of the population will then be inferred
    by trying random values until a good fit on performance is found for training population.

    :param individuals_path: Path to the saved individuals to use.
    :param training_protocol_path: Path to the training protocol to follow.
    :param expected_results: The expected training results in terms of 1RM.
    :returns: The inferred internal model parameters and the resulting accuracy in terms of
    difference between actual and expected performance.
    """

    # load individuals
    individuals = load_individuals(individuals_path)

    # load training protocol
    prescribed_training_df = pd.read_csv(training_protocol_path)

    # construct training instructions to use for simulation for each individual
    individual_training = create_training_dict(individuals, prescribed_training_df)


def create_training_dict(individuals, training_df):
    """Creates a dataframe of specific weights to use for an individual based on their capacity.

    :param individuals: List of individuals to prescribe training.
    :param training_df: Dataframe of prescribed training protocol.

    :returns: Dataframe where percentage of 1RM has been replaced be pre-protocol performance
    weights.
    """
    training_dict = dict()
    for individual in individuals:
        adjusted_training = training_df.copy()
        adjusted_training.loc["Percent1RM"] =
        training_dict[individual] =