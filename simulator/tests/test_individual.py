import pytest
from individual import Individual
import datetime
import pandas as pd

def test_get_age(individual):
    individual.birth = datetime.datetime(datetime.datetime.now().year - 23,1,1)
    assert individual.get_age() == 23

def test_to_dataframe(individual):
    df = individual.to_dataframe()
    ind_df = Individual(df)
    assert individual.__eq__(ind_df)