from datetime import datetime
import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans, fixed_dictionaries, lists, dates

from data_parser import calculate_1rm, split_into_weeks

@given(floats(min_value=0, allow_infinity=False), integers(min_value=0))
def test_calculate_1rm(weight, repetitions):
    real = weight * (1 + (repetitions / 30.0))

    assert real == calculate_1rm(weight, repetitions)


MAPPING = {
    'exercise': integers(min_value=0),
    'weight': floats(min_value=0, allow_infinity=False),
    'repetitions': integers(min_value=0),
    'timestamp': dates(min_value=datetime(1000, 1, 1).date()).map(
        lambda x: datetime.strftime(x, "%m/%d/%Y %H:%M"))
}
@given(lists(fixed_dictionaries(MAPPING)))
def test_split_into_weeks(input_sets):
    """
    Tests the split_into_weeks function.
    """
    date_format = "%m/%d/%Y %H:%M"
    weeks = split_into_weeks(input_sets, date_format)

    # Assertion holds for now since we have same date on all.

    for week, sets in weeks.items():
        for s in sets:
            set_week = datetime.strptime(s.get('timestamp'), date_format).isocalendar()[1]
            assert week == str(set_week)
