
"""Unit tests for the movement module"""

from datetime import timedelta  

def test_set_reps_performed(bench_press):
    """Test that the PC-level has decreased linear after performing a number of repetitions."""
    assert bench_press.current_PC_percentage == 1
    bench_press.set_reps_performed(3,6)
    assert bench_press.current_PC_percentage == 0.5
    bench_press.set_reps_performed(3,6)
    assert bench_press.current_PC_percentage == 0.25

def test_get_PC_recovered_percentage(timestamp,bench_press):
    """Test that the recovered PC percentage varying depending on the rest time between sets."""
    initial_percentage = bench_press.get_PC_recovered_percentage(timestamp)
    second_percentage = bench_press.get_PC_recovered_percentage(timestamp + timedelta(seconds=10))
    bench_press.set_reps_performed(3,6)
    third_percentage = bench_press.get_PC_recovered_percentage(timestamp + timedelta(seconds=40))
    fourth_percentage = bench_press.get_PC_recovered_percentage(timestamp + timedelta(seconds=70))

    assert initial_percentage == 1
    assert second_percentage == 1
    assert third_percentage == 0.75
    assert fourth_percentage == 0.75 + (1-0.75)/2

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

