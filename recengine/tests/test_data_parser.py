"""
Tests for the data_parser module.
"""
from datetime import datetime
import os
import csv

import pytest
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans, fixed_dictionaries, lists, dates

from data_parser import (calculate_1rm,
                         split_into_weeks,
                         calculate_ttrdata_from_week_dict,
                         ttrdata_from_csv,
                         ttrdata_from_csv_bytes,
                         ttr_data_from_reader)

@given(floats(min_value=0, allow_infinity=False), integers(min_value=0))
def test_calculate_1rm(weight, repetitions):
    """
    Tests the calculate_1rm function.
    """
    real = weight * (1 + (repetitions / 30.0))

    assert real == calculate_1rm(weight, repetitions)

DATE_FORMAT = "%m/%d/%Y %H:%M"
MAPPING = {
    'exercise': integers(min_value=0),
    'weight': floats(min_value=0, allow_infinity=False),
    'repetitions': integers(min_value=0),
    'timestamp': dates(min_value=datetime(1000, 1, 1).date()).map(
        lambda x: datetime.strftime(x, DATE_FORMAT))
}
@given(lists(fixed_dictionaries(MAPPING)))
def test_split_into_weeks(input_sets):
    """
    Tests the split_into_weeks function.
    """
    weeks = split_into_weeks(input_sets, DATE_FORMAT)

    # Assertion holds for now since we have same date on all.

    for week, sets in weeks.items():
        for t_set in sets:
            set_week = datetime.strptime(t_set.get('timestamp'), DATE_FORMAT).isocalendar()[1]
            assert week == str(set_week)

@given(lists(fixed_dictionaries(MAPPING)))
def test_calculate_ttrdata_from_week_dict(input_sets):
    """
    Tests the calculate_ttrdata_from_week_dict function.
    """

    weeks = split_into_weeks(input_sets, DATE_FORMAT)
    ttrdata = calculate_ttrdata_from_week_dict(weeks)

    # ttrdata should hold two values per week.
    assert len(weeks.keys()) * 2 == len(ttrdata)


def test_ttrdata_from_csv():
    """
    Tests the ttrdata_from_csv function.
    """
    logs_path = os.path.join(os.path.dirname(__file__), "training_logs", "test.csv")

    ttrdata = ttrdata_from_csv(logs_path, DATE_FORMAT)
    assert len(ttrdata) == 12


def test_ttrdata_from_csv_bytes():
    """
    Tests the ttrdata_from_csv_bytes function.
    """
    logs_path = os.path.join(os.path.dirname(__file__), "training_logs", "test.csv")

    with open(logs_path, 'r') as file:
        ttrdata = ttrdata_from_csv_bytes(file, DATE_FORMAT)
        assert len(ttrdata) == 12


def test_ttr_data_from_reader():
    """
    Tests the ttrdata_from_reader function.
    """
    logs_path = os.path.join(os.path.dirname(__file__), "training_logs", "test.csv")

    with open(logs_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter="|")
        ttrdata = ttr_data_from_reader(csv_reader, DATE_FORMAT)
        assert len(ttrdata) == 12
