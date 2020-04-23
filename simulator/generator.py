"""Module generates a population of individuals based on given population parameters. These
individuals can then be stored away for later use."""

import os
import datetime
import numpy as np
import names
import pandas as pd
from absl import flags
from absl import app
from individual import Individual
from movement import Movement
from gym import BASE_FITNESS_GAIN, BASE_FATIGUE_GAIN, BASE_FITNESS_DECAY, BASE_FATIGUE_DECAY

FLAGS = flags.FLAGS
flags.DEFINE_integer("n", 500, "How many individuals to generate")
flags.DEFINE_float("bpm", 100, "Mean of bench press max")
flags.DEFINE_float("bpv", 5, "Variance in bench press max")
flags.DEFINE_string("p", "simulator/individuals/GeneratedIndividuals.csv",
                    "Full path to save generated individuals in .csv format to")


def random_banister_parameters():
    """
    Uniformly selects parameters for the banister model
    """
    params = {}

    fitness_decay = np.random.randint(
        2, 50)

    # Integer between 1 and fitness_decay (fitness lasts longer than fatigue)
    fatigue_decay = np.random.randint(1, fitness_decay)

    # Float between 1 and 5
    fitness_gain, fatigue_gain = np.random.uniform(
        1, 5, 2)


    # Insert them into the dict and return
    params["fitness_gain"] = fitness_gain
    params["fatigue_gain"] = fatigue_gain
    params["fitness_decay"] = fitness_decay
    params["fatigue_decay"] = fatigue_decay
    return params

def generate_individuals(num, bench_press_fitness_mean, bench_press_fitness_variance):
    """
    Generates individuals to be used in the simulator

    :param num: Number of individuals to generate.
    :param bench_press_fitness_mean: The mean of the 1RM in bench press for the individuals
    :param bench_press_fitness_variance: The variance in the 1RM for the individuals for a normal
    distribution
    :return: A list of individuals generated

    """

    # Holds all individuals
    individuals = []

    # Normally distributed bench press fitnesses used to create bench press movementss
    bench_press_performances = np.random.normal(bench_press_fitness_mean, bench_press_fitness_variance,
                                                num).astype("int")

    banister_params = random_banister_parameters()

    for i in range(num):
        name = names.get_full_name()
        bench_press_movement = Movement(
            0, 0, bench_press_performances[i],
            banister_params["fitness_gain"], banister_params["fatigue_gain"], banister_params["fitness_decay"], banister_params["fatigue_decay"])
        individual = Individual(i,datetime.datetime.now(),name, bench_press_movement)
        individuals.append(individual)

    return individuals


def save_individuals(individuals, csv_file_path, timestamp):
    """Saves individuals for later use in csv file. If given path to csv file already containing
    individuals the function just appends the given individuals to that file.

    :param individuals: List of Individual(s) to save to .csv.
    :param csv_file_path: Path to file name of .csv.
    :param timestamp that denotes the time associated with the current state of the individual.
    """
    all_indviduals_df = pd.DataFrame(columns=['ID', 'Name',
                                              'bench_press_fitness',
                                              'bench_press_fatigue',
                                              'bench_press_basic_performance',
                                              'bench_press_fitness_gain',
                                              'bench_press_fatigue_gain',
                                              'bench_press_fitness_decay',
                                              'bench_press_fatigue_decay',
                                              'Timestamp'
                                              ])
    # check if file is empty
    if os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        all_indviduals_df = all_indviduals_df.append(
            pd.read_csv(csv_file_path, sep="|"))

    for individual in individuals:
        series = individual.to_series()
        series["Timestamp"] = timestamp
        all_indviduals_df = all_indviduals_df.append(series, ignore_index=True)

    # save to given path
    all_indviduals_df.to_csv(csv_file_path, sep="|", index=False)


def load_individuals(individuals_path):
    """Load individuals into list of Individual class instances.

    :param individuals_path: Path to file containing individuals.
    :returns: A list of Individual class instances
    """
    # load individuals from csv file
    individuals_df = pd.read_csv(individuals_path, sep="|")

    # construct objects from entries
    individuals = []
    for _, individual_series in individuals_df.iterrows():
        individuals.append(Individual(series=individual_series))

    return individuals


def generate_individuals_with_param(n, bpm, bpv):

    generated_individuals = generate_individuals(n, bpm, bpv)
    save_individuals(generated_individuals, "simulator/api/individuals/GeneratedIndividuals.csv", datetime.datetime.now())
    save_individuals(generated_individuals, "models/api/individuals/GeneratedIndividuals.csv", datetime.datetime.now())

    print("finish generate_individuals_with_param")


def main(argv):
    """absl entry if user wishes to generate individuals without also training them using the main
    program
    :param argv: Unused, it's required for absl
    """
    del argv  # Unused.
    generated_individuals = generate_individuals(FLAGS.n,
                                                 FLAGS.bpm, FLAGS.bpv)
    save_individuals(generated_individuals, FLAGS.p, datetime.datetime.now())


if __name__ == "__main__":
    app.run(main)
    # print(random_banister_parameters())
    # generate_individuals_with_param(100, 100, 5)
