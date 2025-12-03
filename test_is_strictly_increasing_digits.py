from is_strictly_increasing_digits import *

def test_true_simple():
    assert is_strictly_increasing_digits(13579) is True

def test_false_equal():
    assert is_strictly_increasing_digits(1223) is False

def test_false_desc():
    assert is_strictly_increasing_digits(321) is False

def test_single_digit_and_zero():
    assert is_strictly_increasing_digits(0) is True
    assert is_strictly_increasing_digits(7) is True

def test_invalid_cases():
    assert is_strictly_increasing_digits(-1) == -1
    assert is_strictly_increasing_digits(3.0) == -1

def test_large_true():
    assert is_strictly_increasing_digits(123456789) is True


