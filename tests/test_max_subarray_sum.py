import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_case():
    """Test a standard case with a typical input."""
    assert max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == [39]

def test_small_array():
    """Test with a smaller array."""
    assert max_subarray_sum([2, 3, 4, 1, 5], 2) == [7]

def test_k_larger_than_list():
    """Test when k is larger than the list length."""
    assert max_subarray_sum([1, 2, 3], 4) == []

def test_k_equal_list_length():
    """Test when k is equal to the list length."""
    assert max_subarray_sum([1, 2, 3], 3) == [6]

def test_single_element_list():
    """Test with a single-element list."""
    assert max_subarray_sum([5], 1) == [5]

def test_empty_list():
    """Test with an empty list."""
    assert max_subarray_sum([], 0) == []

def test_negative_numbers():
    """Test with negative numbers."""
    assert max_subarray_sum([-1, -2, -3, 4, 5, -6], 2) == [9]

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -3, 2, 4, -1, 5], 3) == [10]

def test_invalid_inputs():
    """Test with invalid inputs that should raise an error."""
    with pytest.raises(TypeError):
        max_subarray_sum(None, 2)
    
    with pytest.raises(TypeError):
        max_subarray_sum([1, 2, 3], None)