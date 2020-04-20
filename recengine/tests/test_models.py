"""
These tests ensures that the previously existed models for training programs exists.
The tests makes it so that it is impossible to remove a model by mistake since tests
will fail.
"""
import pytest
import os

def test_required_models_exist_pbar():
    """
    Tests that the required models for pbar
    exists in the correct folder.
    """
    folder_path = os.path.join(os.path.dirname(__file__), os.pardir, "pbar")

    assert os.path.exists(os.path.join(folder_path, "ogasawara_HL.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "ogasawara_LL.sav")) is True

def test_required_models_exist_ttr():
    """
    Tests that the required models for ttr
    exists in the correct folder.
    """
    folder_path = os.path.join(os.path.dirname(__file__), os.pardir, "ttr")

    assert os.path.exists(os.path.join(folder_path, "ogasawara_HL.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "ogasawara_LL.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "6w_bp_fiesta.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "carls_power_program_BP.sav")) is True
    assert os.path.exists(os.path.join(folder_path, "kikuchi.sav")) is True
