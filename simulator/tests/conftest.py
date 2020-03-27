"""Pylint test configuration file"""
# pylint: disable=redefined-outer-name

import datetime
from datetime import datetime
import pytest
import pandas as pd
from individual import Individual
from movement import Movement


@pytest.fixture()
def bench_press():
    """Fixture for sample bench press movement with set parameters"""
    return Movement(fitness=0, fatigue=0, basic_performance=300, fitness_gain=1, fatigue_gain=1,
                    fitness_decay=1, fatigue_decay=0.99)


@pytest.fixture()
def individual(bench_press):
    """Fixture for sample individual with set parameters"""
    return Individual(id=0, birth=datetime(1, 1, 1), gender=1, name="Juliana Maddox", weight=40,
                      bench_press_movement=bench_press)


@pytest.fixture()
def timestamp():
    """Fixture for sample timestamp with set parameters"""
    return datetime.strptime("02/02/2010 12:00", "%d/%m/%Y %H:%M")


@pytest.fixture()
def training_dataframe(timestamp):
    """Fixture for sample dataframe of training program"""
    column_names = ["Weight", "Reps", "Timestamp"]
    return pd.DataFrame([[200, 3, timestamp]], columns=column_names)


@pytest.fixture()
def impossible_training_dataframe(timestamp):
    """Fixture for sample dataframe of impossible training program"""
    column_names = ["Weight", "Reps", "Timestamp"]
    return pd.DataFrame([[999999, 999999, timestamp]], columns=column_names)
