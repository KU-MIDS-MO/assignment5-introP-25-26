from count_digits_greater_than import *

def test_examples():
    assert count_digits_greater_than(12345, 3) == 2  # 4,5
    assert count_digits_greater_than(1111, 7) == 0
    assert count_digits_greater_than(9876, 0) == 4

def test_zero_and_threshold():
    assert count_digits_greater_than(0, 0) == 0

def test_invalid():
    assert count_digits_greater_than(-1, 3) == -1
    assert count_digits_greater_than(123, -1) == -1
    assert count_digits_greater_than(123, 10) == -1
    assert count_digits_greater_than(123, 2.5) == -1

def test_large_pattern():
    assert count_digits_greater_than(909090909, 8) == 5
    assert count_digits_greater_than(909090909, 0) == 5
