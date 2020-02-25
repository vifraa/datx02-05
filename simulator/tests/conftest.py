import pytest
import datetime
from individual import Individual
from movement import Movement
from gym import TrainingSet


@pytest.fixture()
def bench_press():
    '''Fixture for sample bench press movement with set parameters'''
    return Movement(fitness=300, fatigue=0, performance=300, fitness_gain=1, fatigue_gain=1, fitness_decay=1,
                    fatigue_decay=0.99)


@pytest.fixture()
def individual(bench_press):
    '''Fixture for sample individual with set parameters'''
    return Individual(id=0, birth=datetime.date(1, 1, 1), gender=1, name="Juliana Maddox", weight=40,
                      bench_press_movement=bench_press)


@pytest.fixture()
def training_list():
    '''Fixture for sample list of TrainingSets performed'''
    return [[TrainingSet(weight=200, reps=3)]]


@pytest.fixture()
def impossible_training_list():
    '''Fixture for sample list of TrainingSets performed'''
    return [[TrainingSet(weight=99999999, reps=99999999)]]
