
"""Unit tests for the movement module"""

from datetime import timedelta  

def test_get_PC_recovered_percentage(timestamp,bench_press):
    """Test that the recovered PC percentage varying depending on the rest time between sets."""
    initial_percentage = bench_press.get_PC_recovered_percentage(timestamp)
    second_percentage = bench_press.get_PC_recovered_percentage(timestamp + timedelta(seconds=10))
    third_percentage = bench_press.get_PC_recovered_percentage(timestamp + timedelta(minutes=3))

    assert initial_percentage == 1
    assert second_percentage < initial_percentage
    assert third_percentage > second_percentage

def test_amrap_high_intensity(bench_press):
    """Test to see that behaviour of Mayhew's formula is reasonable at high intensities"""
    assert bench_press.amrap(300) == 1
    assert bench_press.amrap(301) == 0

def test_amrap_mid_intensity(bench_press):
    """Test to see that behaviour of Mayhew's formula is reasonable at intermediate intensities"""
    assert bench_press.amrap(300*0.89) == 2
    assert bench_press.amrap(300*0.85) == 4

def test_amrap_low_intensity(bench_press):
    """Test to see that behaviour of Mayhew's formula is reasonable at low intensities"""
    assert bench_press.amrap(300*0.7) == 11
    assert bench_press.amrap(0) == 11

