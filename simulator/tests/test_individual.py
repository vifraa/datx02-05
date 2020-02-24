import pytest
from individual import Individual
import datetime


@pytest.fixture()
def individual():
    '''Fixture for sample individual with set parameters'''
    return Individual(id=0, birth= datetime.datetime(1995,2,3), gender=1, name="Juliana Maddox", weight=40, bench_press_movement=20)


def test_get_age():
    ind = individual()
    ind.birth = datetime.datetime(datetime.datetime.now().year - 23,1,1)
    assert ind.get_age == 23

def test_to_dataframe():
    #memes