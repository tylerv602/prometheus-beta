import pytest
from src.array_min import find_minimum

def test_find_minimum_positive_numbers():
    """Test finding minimum in an array of positive numbers."""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([100, 50, 75, 25]) == 25

def test_find_minimum_negative_numbers():
    """Test finding minimum in an array with negative numbers."""
    assert find_minimum([-1, -2, -3, -4, -5]) == -5
    assert find_minimum([0, -1, -2, 1, 2]) == -2

def test_find_minimum_mixed_numbers():
    """Test finding minimum in an array with mixed positive and negative numbers."""
    assert find_minimum([-10, 0, 10, 20]) == -10
    assert find_minimum([5, -5, 5, -5]) == -5

def test_find_minimum_single_element():
    """Test finding minimum in an array with a single element."""
    assert find_minimum([42]) == 42

def test_find_minimum_with_floats():
    """Test finding minimum in an array with floating-point numbers."""
    assert find_minimum([1.5, 2.3, 0.1, 4.7]) == 0.1

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(123)

def test_non_numeric_elements_raises_error():
    """Test that arrays with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None])