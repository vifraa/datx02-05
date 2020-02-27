import pytest
from individual import Individual
import datetime
import pandas as pd


@pytest.fixture()
def individual():
    '''Fixture for sample individual with set parameters'''
    return Individual(id=0, birth= datetime.datetime(1995,2,3), gender=1, name="Juliana Maddox", weight=40, bench_press_movement=20)

@pytest.fixture()
def individual_df(df):
    '''Fixture for sample individual from dataframe'''
    return Individual(dataframe=df)


def test_get_age():
    ind = individual()
    ind.birth = datetime.datetime(datetime.datetime.now().year - 23,1,1)
    assert ind.get_age == 23

def test_to_dataframe():
    ind = individual()
    df = ind.to_dataframe()
    ind_df = individual_df(df)
    assert ind == ind_df