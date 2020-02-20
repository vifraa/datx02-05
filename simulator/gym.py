import math
from collections import namedtuple

TrainingSet = namedtuple("TrainingSet", "weight, reps")

def train(training_program_path, individual):
'''Function uses an implementation of the Banister model to
adjust fitness and fatigue of an individual by decomposing
a given training program into loads, and then feeding those
to the individual.

:param training_program_path: a path to a csv_file containing a
training program.

:param individual: an Individual class instance

'''
    training_list = load_training(training_program)
    performed_training_list = [[can_do(training_set, individual) for training_set in training_day] for training_day in training_list]

    # train the bench press
    apply_banister(performed_training_list, individual.bench_press)

def apply_banister(training_list, movement):
'''Banister model applied to an instance of Movement class.

:param training_list: a list of performed TrainingSet tuples over time
:param movement: an instance of the Movement class

'''

    for training_day in training_list:
        trimp = generate_trimp(training_day, movement.performance)
        movement.fitness     = movement.fitness * math.exp(-1/movement.fitness_decay) + trimp
        movement.fatigue     = movement.fatigue * math.exp(-1/movement.fatigue_decay) + trimp
        movement.performance = movement.fitness * movement.fitness_gain - movement.fatigue * movement.fatigue_gain


def generate_trimp(training, performance):
'''Create load from given training.

:param training: a list of the TrainingSet tuples performed during training
:param performance: an individuals 1RM

:returns: a scalar value denoting the load of the given training

'''
    cumulative_load = 0
    for training_set in training:
        cumulative_load += training_set.reps * training_set.weight / performance

    return cumulative_load



def can_do(training_set, individual):
'''Takes a requested training set and returns what the set that the
individual is theoretically capable of doing.

:param training_set: a TrainingSet tuple to perform
:param individual: an Individual class instance

:returns: training set that was possible to perform

'''
    reps_possible = individual.amrap(training_set.weight)
    if reps_possible < training_set.reps:
        return TrainingSet(training_set.weight, reps_possible)
    else:
        return training_set


def load_training(path_to_program):
'''Load training program into python list structure from csv.

:param path_to_program: path to training program csv

:returns: python list of days containing TrainingSet tuples

'''
   return None
