import pytest
import tempfile
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans
import os
import csv
import math
import datetime

from model import Model
from recengine import fetch_program_from_model, _create_program_from_csv_reader


def test_fetch_program_bad_input():
    model_path = os.path.join(os.path.dirname(__file__), "models", "programdoesnotexist.sav")
    model = Model(model_path)
    program = fetch_program_from_model(model)
    assert program == {}

def test_fetch_program_from_model():
    model_path = os.path.join(os.path.dirname(__file__), "models", "ogasawara_HL.sav")
    model = Model(model_path)
    program = fetch_program_from_model(model)

    assert program is not None
    assert len(program) == 18

    # Assertions for program rows structure
    for _day, sets in program.items():
        for p_set in sets:

            assert isinstance(p_set.exercise, int)
            assert isinstance(p_set.percent_1rm, float)
            assert isinstance(p_set.repetitions, int)

        # Assert all sets in same day actual is done on the same
        # day.
        previous_set_date = None
        for p_set in sets:
            if previous_set_date is None:
                previous_set_date = p_set.date
                continue

            today = p_set.date
            assert previous_set_date == today

def test_correctly_calculated_rest():
    """
    Tests that the calculated rest is correct.
    """
    program_path = os.path.join(os.path.dirname(__file__), "training_programs", "ogasawara_HL.csv")

    with open(program_path, newline='') as file:
        program_reader = csv.reader(file, delimiter="|")
        _headers = next(program_reader)

        program = _create_program_from_csv_reader(program_reader)
        for _day, sets in program.items():
            for p_set in sets:
                assert isinstance(p_set.rest, float)
                assert math.isclose(p_set.rest, 3.0)
