import datetime
from individual import Individual




def test_to_series(individual):
    """Test if a new individual initialized from an individual's generated series is equals to eachother."""
    series = individual.to_series()
    ind_series = Individual(series)
    assert individual.__eq__(ind_series)

