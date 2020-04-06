import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans

from data_parser import calculate_1rm

@given(floats(min_value=0, allow_infinity=False), integers(min_value=0))
def test_calculate_1rm(weight, repetitions):
    real = weight * (1 + (repetitions / 30.0))

    assert real == calculate_1rm(weight, repetitions)



