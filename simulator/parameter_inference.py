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
    individual_training = create_training_dict(
        individuals, prescribed_training_df)


def create_training_dict(individuals, training_df):
    """Creates a dictionary of specific weights to use for an individual based on their capacity.

    :param individuals: List of individuals to prescribe training.
    :param training_df: Dataframe of prescribed training protocol.

    :returns: Dataframe where percentage of 1RM has been replaced be pre-protocol performance
    weights.
    """
    training_dict = dict()
    for individual in individuals:
        adjusted_training = training_df.copy()

        # Get the individually adjusted weights
        specific_weights = get_weights_from_percent(
            individual, adjusted_training["Percent1RM"])

        # Set them in the program and adjust column name
        adjusted_training["Percent1RM"] = specific_weights
        adjusted_training.rename(
            columns={'Percent1RM': 'Weight'}, inplace=True)
        training_dict[individual] = adjusted_training

    return training_dict


def get_weights_from_percent(individual, percentages):
    """

    Given a list of percentages, return a list of real weights for the individual.

    :param individual: The invidiual to calculate weights for.
    :param percentages: Percentages of 1RM in the program.
    """
    # This is using performance, perhaps we should use fitness instead?
    return [individual.bench_press_movement.performance*(percent/100) for percent in percentages]


if __name__ == "__main__":
    infer_model_parameters("simulator/individuals/GeneratedIndividuals.csv",
                           "simulator/training_programs/ogasawara.csv", None)
