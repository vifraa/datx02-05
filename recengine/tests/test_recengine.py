import pytest
import tempfile
from hypothesis import given
from hypothesis.strategies import floats, integers, sampled_from, booleans
import os
import datetime

from model import Model
from recengine import fetch_program_from_model


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
    for day, sets in program.items():
        for p_set in sets:

            # These assorts are quite useless at the moment but will
            # will make tests fail later when we refactor into
            # a proper set datastructure.
            assert isinstance(p_set[0], str)
            assert isinstance(p_set[1], str)
            assert isinstance(p_set[2], str)
            assert isinstance(p_set[3], str)

            assert isinstance(int(p_set[0]), int)
            assert isinstance(int(p_set[1]), int)
            assert isinstance(int(p_set[2]), int)

            try:
                datetime.datetime.strptime(p_set[3], "%m/%d/%Y %H:%M")
            except ValueError:
                pytest.fail("Timestamp format is not correct.")

        previous_set_date = None
        for p_set in sets:
            if previous_set_date is None:
                previous_set_date = datetime.datetime.strptime(p_set[3], "%m/%d/%Y %H:%M")
                continue

            today = datetime.datetime.strptime(p_set[3], "%m/%d/%Y %H:%M")
            assert previous_set_date < today
