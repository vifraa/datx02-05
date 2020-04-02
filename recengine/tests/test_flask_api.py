import pytest
from hypothesis import given, settings
from hypothesis.strategies import floats, integers, sampled_from, booleans

import flask_api

@pytest.fixture
def client():
    with flask_api.app.test_client() as client:
        yield client

@given(integers(min_value=0), floats(min_value=0, allow_infinity=False),
       floats(min_value=0, allow_infinity=False),
       sampled_from(["MAN", "WOMAN", "OTHER"]))
@settings(deadline=500)
def test_pbar(client, age, weight, performance, sex):
    res = client.post("/api/v1/pbar", json={
        "age": age,
        "weight": weight,
        "sex": sex,
        "performance": performance
    })
    json_res = res.get_json()
    assert json_res["training_program"] is not None
    assert isinstance(json_res["training_program"], str)

    assert json_res["predicted_performance"] is not None
    assert isinstance(json_res["predicted_performance"], float)

    assert json_res["program_structure"] is not None
    assert isinstance(json_res["program_structure"], dict)
