from sum_of_cubes_even import *
import math

def test_zero():
    assert sum_of_cubes_even(0) == 0.0

def test_small():
    # 2^3 + 4^3 + 6^3 = 8 + 64 + 216 = 288
    assert sum_of_cubes_even(6) == 288.0

def test_odd_boundary():
    assert sum_of_cubes_even(7) == 288.0

def test_invalid():
    assert sum_of_cubes_even(-5) == -1
    assert sum_of_cubes_even(2.2) == -1

def test_warn_and_compute(capsys):
    res = sum_of_cubes_even(2002)
    out = capsys.readouterr().out.lower()
    assert "warning" in out
    assert isinstance(res, float) and res > 0.0

def test_type_float():
    assert isinstance(sum_of_cubes_even(10), float)
