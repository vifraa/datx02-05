import math
import numpy as np
import pandas as pd
from individual import Individual
from generator import load_individuals
import gym


def infer_model_parameters(individuals_path, training_protocol_path, performance_gain_mean, performance_gain_std):
    """Run training study in accordance to given population parameters, training protocols and
    expected results. The internal modelling parameters of the population will then be inferred
    by trying random values until a good fit on performance is found for training population.

    :param individuals_path: Path to the saved individuals to use.
    :param training_protocol_path: Path to the training protocol to follow.
    :param performance_gain_mean: The mean of peformance increases in terms of 1RM.
    :param performance_gain_std: The standard deviation of performance increases in terms of 1RM.
    :returns: The inferred internal model parameters and the resulting accuracy in terms of
    difference between actual and expected performance.
    """

    # load individuals
    pre_training_individuals = load_individuals(individuals_path)

    # load training protocol
    prescribed_training_df = gym.load_training(training_protocol_path)

    # construct training instructions to use for simulation for each individual
    individual_training = create_training_dict(
        pre_training_individuals, prescribed_training_df)

    # Train individuals with randomized parameters and see if results are correct
    while (True):  # While results not met
        individuals = pre_training_individuals.copy()

        # Generate random parameters
        fitness_decay = np.random.randint(
            1, 50)

        # Integer between 1 and fitness_decay (fitness lasts longer than fatigue)
        fatigue_decay = np.random.randint(1, fitness_decay)

        # Float between 1 and 5
        fitness_gain, fatigue_gain = np.random.uniform(
            1, 5, 2)
        print(fitness_decay, fatigue_decay, fitness_gain, fatigue_gain)
        # Set same parameters to each individual and train them
        for individual in individuals:
            individual.bench_press_movement.fitness_decay = fitness_decay
            individual.bench_press_movement.fatigue_decay = fatigue_decay
            individual.bench_press_movement.fitness_gain = fitness_gain
            individual.bench_press_movement.fatigue_gain = fatigue_gain
            gym.train(individual_training[individual], individual)
        print(calculate_performance_gain_mean(
            pre_training_individuals, individuals))


def calculate_performance_gain_mean(pre_training_individuals, post_training_individuals):
    """
    Given a set of individuals pre training and post training, calculates the mean in performance gain in terms of KG and 1RM.

    :param pre_training_individuals: Individuals before training.
    :param post_training individuals: Individuals after training.
    """

    total_gains = 0
    for i in range(len(pre_training_individuals)):
        pre_training_performance = pre_training_individuals[i].bench_press_movement.performance
        post_training_performance = post_training_individuals[i].bench_press_movement.performance
        diff = math.fabs(post_training_performance-pre_training_performance)
        total_gains += diff
        print("diff:", diff)
    return total_gains/(len(pre_training_individuals))


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
                           "simulator/training_programs/ogasawara.csv", 10, 5)
