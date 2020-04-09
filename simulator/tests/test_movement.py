
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
