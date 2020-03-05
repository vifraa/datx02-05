"""Module provides an environment for observing training effects on trainees by following a given
training program. Training effects are simulated using the Banister model. Though an individual
may be prescribed any training, the module tries to simulate the fact that some training may not be
feasible for the trainee."""

import math
import pandas as pd


def train(training_program_path, individual):
    """Function uses an implementation of the Banister model to
    adjust fitness and fatigue of an individual by decomposing
    a given training program into loads, and then feeding those
    to the individual. The actual performed training logs are
    then returned.

    :param training_program_path: a path to a csv_file containing a
    training program.

    :param individual: an Individual class instance

    :returns: list of performed training logs with current level of performance

    """
    training_dataframe = load_training(training_program_path)

    # train the bench press
    performed_training_dataframe = apply_banister(training_dataframe,
                                                  individual.bench_press_movement)

    return performed_training_dataframe


def apply_banister(training_dataframe, movement):
    """Banister model applied to an instance of Movement class.

    :param training_dataframe: a dataframe of performed training sets over time
    :param movement: an instance of the Movement class

    :returns: a dataframe containing the actual performed training with performance at every step

    """

    # iterate through all prescribed sets
    previous_date = training_dataframe["Timestamp"].iloc[0].date()
    cumulative_trimp = 0
    performed_training = training_dataframe.copy()

    # add column for current level of performance
    performed_training["Performance"] = [0] * len(performed_training)

    for index, training_set in training_dataframe.iterrows():

        # convert training to what would be possible for the individual to perform
        training_set = can_do(training_set, movement)
        performed_training.iloc[index, :] = training_set

        # add current level of performance to log
        index_label = training_dataframe.index[index]
        performed_training.loc[index_label,
                               "Performance"] = movement.performance

        # since our timestep is daily, we have to accumulate the training sets taken place during
        # the same day in our calculations
        if training_set["Timestamp"].date() > previous_date:

            # apply training effects from previous training day
            apply_training_effects(movement, cumulative_trimp)

            # reset training load for next day
            cumulative_trimp = 0

            # iterate through eventual rest-days where no training is performed
            delta = training_set["Timestamp"].date() - previous_date.date()
            rest_days = delta.days
            for _ in range(rest_days):
                apply_training_effects(movement, cumulative_trimp)

        else:
            cumulative_trimp = generate_trimp(
                training_set, movement.performance)

        previous_date = training_set["Timestamp"].date()

    # finally apply any training effects acummulated at end
    if cumulative_trimp > 0:
        apply_training_effects(movement, cumulative_trimp)

    # return actual performed training
    return performed_training


def apply_training_effects(movement, cumulative_trimp):
    """Apply trimp to affect movement parameters according to the Banister model.

    :param movement: an instance of the Movement class
    :param cumulative_trimp: trimp to apply to Movement parameters

    """

    movement.fitness = movement.fitness * \
        math.exp(-1 / movement.fitness_decay) + cumulative_trimp
    movement.fatigue = movement.fatigue * \
        math.exp(-1 / movement.fatigue_decay) + cumulative_trimp
    movement.performance = movement.fitness * movement.fitness_gain - \
        movement.fatigue * movement.fatigue_gain


def generate_trimp(training_set, performance):
    """Create load from given training.

    :param training_set: a pandas Series representing a training set
    :param performance: an individuals 1RM

    :returns: a scalar value denoting the load of the given training set

    """

    load = training_set["Reps"] * training_set["Weight"] / performance
    return load


def can_do(training_set, movement):
    """Takes a requested training set and returns what the set that the
    individual is theoretically capable of doing.

    :param training_set: a pandas Series representing the training set to perform
    :param movement: a Movement class instance

    :returns: a pandas Series representing the training set that was possible to perform

    """

    reps_possible = movement.amrap(training_set["Weight"])
    if reps_possible < training_set["Reps"]:
        training_set["Reps"] = reps_possible
    return training_set


def load_training(path_to_program):
    """Load training program into python list structure from csv.

    :param path_to_program: path to training program csv

    :returns: pandas dataframe of days containing training sets

    """

    training_frame = pd.read_csv(path_to_program, sep="|")

    # make timestamp column more conveniently usable
    training_frame["Timestamp"] = pd.to_datetime(training_frame["Timestamp"])
    return training_frame
