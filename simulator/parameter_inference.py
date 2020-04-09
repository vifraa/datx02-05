import math
import numpy as np
import pandas as pd
from individual import Individual
from generator import load_individuals
import gym
from matplotlib import pyplot as plt
import copy


def infer_model_parameters(individuals_path, training_protocol_path,
                           performance_gain_mean, performance_gain_std, threshold):
    """Run training study in accordance to given population parameters, training protocols and
    expected results. The internal modelling parameters of the population will then be inferred
    by trying random values until a good fit on performance is found for training population.

    :param individuals_path: Path to the saved individuals to use.
    :param training_protocol_path: Path to the training protocol to follow.
    :param performance_gain_mean: The mean of peformance increases in terms of 1RM.
    :param performance_gain_std: The standard deviation of performance increases in terms of 1RM.
    :param threshold: The allowed difference between expected and actual mean and standard
    deviation in performance gains.
    :returns: The inferred internal model parameters and the resulting accuracy in terms of
    difference between actual and expected performance.
    """

    # load individuals
    pre_training_individuals = load_individuals(individuals_path)

    # construct training instructions to use for simulation for each individual
    individual_training = create_training_dict(
        pre_training_individuals, training_protocol_path)

    # parameters to estimate
    fitness_gain = 0
    fatigue_gain = 0
    fitness_decay = 0
    fatigue_decay = 0

    delta = 99999999999
    best_delta = delta
    iteration_mean = 0
    iteration_stdev = 0

    # Train individuals with randomized parameters and see if results are correct
    while delta > threshold:
        post_training_individuals = [copy.deepcopy(individual)
                                     for individual in pre_training_individuals]

        # Generate random parameters
        fitness_decay = np.random.randint(
            2, 50)

        # Integer between 1 and fitness_decay (fitness lasts longer than fatigue)
        fatigue_decay = np.random.randint(1, fitness_decay)

        # Float between 1 and 5
        fitness_gain, fatigue_gain = np.random.uniform(
            1, 5, 2)
        # Set same parameters to each individual and train them
        for individual in post_training_individuals:
            individual.bench_press_movement.fitness_decay = fitness_decay
            individual.bench_press_movement.fatigue_decay = fatigue_decay
            individual.bench_press_movement.fitness_gain = fitness_gain
            individual.bench_press_movement.fatigue_gain = fatigue_gain
            gym.train(individual_training[individual.id], individual)
        iteration_mean, iteration_stdev = \
            calculate_performance_gain_distribution(pre_training_individuals,
                                                    post_training_individuals)

        delta = abs(performance_gain_mean - iteration_mean) + \
            abs(performance_gain_std - iteration_stdev)

        best_delta = min(delta, best_delta)

        # update user on progress
        print("Current iteration delta: {}".format(delta))
        print("Best delta so far: {}".format(best_delta))

    print("Distribution mean error: {}".format(
        abs(iteration_mean-performance_gain_mean)))
    print("Distribution standard deviation error: {}".format(
        abs(iteration_stdev-performance_gain_std)))
    print("fitness_gain: {}".format(fitness_gain))
    print("fatigue_gain: {}".format(fatigue_gain))
    print("fitness_decay: {}".format(fitness_decay))
    print("fatigue_decay: {}".format(fatigue_decay))

    # parameters have been found
    return (fitness_gain, fatigue_gain, fitness_decay, fatigue_decay)


def calculate_performance_gain_distribution(pre_training_individuals, post_training_individuals):
    """
    Given a set of individuals pre training and post training, calculates the mean in performance gain in terms of KG and 1RM.

    :param pre_training_individuals: Individuals before training.
    :param post_training individuals: Individuals after training.

    :returns: tuple of performance gain mean and standard deviation
    """

    changes = []
    for i in range(len(pre_training_individuals)):
        pre_training_performance = \
            pre_training_individuals[i].bench_press_movement.get_current_performance(
            )
        post_training_performance = \
            post_training_individuals[i].bench_press_movement.get_current_performance(
            )
        diff = post_training_performance-pre_training_performance
        changes.append(diff)

    return np.mean(changes), np.std(changes)


def create_training_dict(individuals, program_path):
    """Creates a dictionary of specific weights to use for an individual based on their capacity.

    :param individuals: List of individuals to prescribe training.
    :param program_path: file path to program

    :returns: Dataframe where percentage of 1RM has been replaced be pre-protocol performance
    weights.
    """
    training_dict = dict()
    for individual in individuals:

        training_dict[individual.id] = gym.load_training(
            program_path, individual.bench_press_movement)

    return training_dict


def get_weights_from_percent(individual, percentages):
    """

    Given a list of percentages, return a list of real weights for the individual.

    :param individual: The invidiual to calculate weights for.
    :param percentages: Percentages of 1RM in the program.
    """
    # This is using performance, perhaps we should use fitness instead?
    return [individual.bench_press_movement.get_current_performance()
            * (percent/100) for percent in percentages]


if __name__ == "__main__":
    params_og_HL = []
    params_og_LL = []
    params_kik = []
    for i in range(100):
        params_og_HL.append(infer_model_parameters("simulator/training_programs/ogasawara_HL_pop.csv",
                                                   "simulator/training_programs/ogasawara_HL.csv", 10.5, 2.95, 5))

        # params_og_LL.append(infer_model_parameters("simulator/training_programs/ogasawara_LL_pop.csv",
        # "simulator/training_programs/ogasawara_LL.csv", 5.2, 1.7, 5))
        # params_kik.append(infer_model_parameters("simulator/training_programs/kikuchi_pop.csv",
        # "simulator/training_programs/kikuchi.csv", 5.0, 12.1, 5))
    fi_g = [item[0] for item in params_og_HL]
    fa_g = [item[1] for item in params_og_HL]
    fi_d = [item[2] for item in params_og_HL]
    fa_d = [item[3] for item in params_og_HL]

    plt.hist(fi_g)
    plt.show()
