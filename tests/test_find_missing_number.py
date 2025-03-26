import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test finding a missing number in a basic sequence."""
    assert find_missing_number([1, 3, 4, 5]) == 2

def test_find_missing_number_full_sequence():
    """Test finding a missing number at the end of a full sequence."""
    assert find_missing_number([1, 2, 3, 4, 5]) == 6

def test_find_missing_number_first_number():
    """Test finding a missing first number."""
    assert find_missing_number([2, 3, 4, 5]) == 1

def test_find_missing_number_large_sequence():
    """Test finding a missing number in a larger sequence."""
    nums = list(range(1, 11))
    nums.remove(7)
    assert find_missing_number(nums) == 7

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_missing_number([])

def test_invalid_input_non_list():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_missing_number("not a list")

def test_invalid_input_non_integers():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_number([1, 2, "3", 4])

def test_invalid_input_floats():
    """Test that a list with float elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_number([1.0, 2.0, 3.0])