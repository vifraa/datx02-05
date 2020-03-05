import datetime
from individual import Individual


def test_get_age(individual):
    """Test if the returned age is correct"""
    individual.birth = datetime.datetime(
        datetime.datetime.now().year - 23, 1, 1)
    assert individual.get_age() == 23


def test_to_series(individual):
    """Test if a new individual initialized from an individual's generated series is equals to eachother."""
    series = individual.to_series()
    ind_series = Individual(series)
    assert individual.__eq__(ind_series)

