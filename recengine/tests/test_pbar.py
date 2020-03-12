import pytest
import os

def test_required_models_exist():
    """
    Tests that the required models for pbar
    exists in the correct folder.
    """
    folder_path = os.path.join(os.path.dirname(__file__), os.pardir, "pbar")

    # The check if these files exists is only used temporary until we generate 
    # models for different exercises. These test makes sure that the recommendation
    # engine is runnable.
    assert os.path.exists(os.path.join(folder_path, "bench_lasso.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "bench_ridge.sav")) is True
