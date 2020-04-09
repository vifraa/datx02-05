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
flags.DEFINE_integer("n", 2, "How many individuals to generate")
flags.DEFINE_float("bpm", 100, "Mean of bench press max")
flags.DEFINE_float("bpv", 5, "Variance in bench press max")
flags.DEFINE_integer("am", 30, "Age mean")
flags.DEFINE_integer("av", 5, "Age variance")
flags.DEFINE_float("gr", 0.5, "Gender ratio of male")
flags.DEFINE_string("p", "simulator/individuals/GeneratedIndividuals.csv",
                    "Full path to save generated individuals in .csv format to")
flags.DEFINE_float("wm", 50, "Weight mean")
flags.DEFINE_float("wv", 5, "Weigt variance")


def gender_to_string(sex_coding):
    """Returns string representing sex coding
    :param sex_coding: integer representing sex
    :returns: string representing sex"""
    if sex_coding == 0:
        return "male"

    return "female"


def generate_individuals(num, age_mean, age_variance, weight_mean, weight_variance,
                         bench_press_fitness_mean, bench_press_fitness_variance, gender_ratio):
    """
    Generates individuals to be used in the simulator

    :param num: Number of individuals to generate.
    :param age_mean: The mean of the age for the individuals
    :param age_variance: The variance in age for the individuals for a normal distribution
    :param bench_press_fitness_mean: The mean of the 1RM in bench press for the individuals
    :param bench_press_fitness_variance: The variance in the 1RM for the individuals for a normal
    distribution
    :param gender_ratio: The ratio of individuals with female sex characteristics
    :return: A list of individuals generated

    """

    # Holds all individuals
    individuals = []

    # Normally distributed ages used to create birth dates
    ages = np.random.normal(age_mean, age_variance, num).astype("int")
    now = datetime.datetime.now()
    try:
        birth_dates = [datetime.datetime(
            now.year - age, now.month, now.day) for age in ages]
    except ValueError:
        # Date could not be set, defaulting
        birth_dates = [datetime.datetime(now.year - age, 1, 1) for age in ages]
    # Normally distributed bench press fitnesses used to create bench press movementss
    bench_press_performances = np.random.normal(bench_press_fitness_mean, bench_press_fitness_variance,
                                                num).astype("int")
    weights = np.random.normal(weight_mean, weight_variance, num)
    genders = np.ones(num)
    genders[:int(num * gender_ratio)] = 0
    np.random.shuffle(genders)
    for i in range(num):
        name = names.get_full_name(gender=gender_to_string(genders[i]))
        bench_press_movement = Movement(
            0, 0, bench_press_performances[i],
            BASE_FITNESS_GAIN, BASE_FATIGUE_GAIN, BASE_FITNESS_DECAY, BASE_FATIGUE_DECAY)
        individual = Individual(i, birth_dates[i], int(genders[i]),
                                name, weights[i], bench_press_movement)
        individuals.append(individual)

    return individuals


def save_individuals(individuals, csv_file_path, timestamp):
    """Saves individuals for later use in csv file. If given path to csv file already containing
    individuals the function just appends the given individuals to that file.

    :param individuals: List of Individual(s) to save to .csv.
    :param csv_file_path: Path to file name of .csv.
    :param timestamp that denotes the time associated with the current state of the individual.
    """
    all_indviduals_df = pd.DataFrame(columns=['ID', 'Birth', 'Gender', 'Name', 'Weight',
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


def main(argv):
    """absl entry if user wishes to generate individuals without also training them using the main
    program
    :param argv: Unused, it's required for absl
    """
    del argv  # Unused.
    generated_individuals = generate_individuals(FLAGS.n, FLAGS.am, FLAGS.av, FLAGS.wm, FLAGS.wv,
                                                 FLAGS.bpm, FLAGS.bpv, FLAGS.gr)
    save_individuals(generated_individuals, FLAGS.p, datetime.datetime.now())


if __name__ == "__main__":
    app.run(main)
