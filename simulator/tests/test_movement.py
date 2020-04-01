
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