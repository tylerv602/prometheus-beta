import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element."""
    assert max_subarray_sum([42]) == 42

def test_alternating_numbers():
    """Test with alternating positive and negative numbers."""
    assert max_subarray_sum([-2, 3, -4, 5, -1]) == 5

def test_with_zeros():
    """Test with array containing zeros."""
    assert max_subarray_sum([0, 0, 0, 1, -1]) == 1

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum(123)

def test_empty_list():
    """Test raising ValueError for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])