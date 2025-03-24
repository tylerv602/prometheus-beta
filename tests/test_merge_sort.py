import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from merge_sort import merge_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert merge_sort([5]) == [5]

def test_sorted_list():
    """Test sorting an already sorted list."""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a reverse-sorted list."""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    """Test sorting a randomly unsorted list."""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert merge_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert merge_sort([-3, 4, -1, 7, -5, 0]) == [-5, -3, -1, 0, 4, 7]

def test_large_list():
    """Test sorting a larger list."""
    large_list = list(range(100, 0, -1))
    assert merge_sort(large_list) == list(range(1, 101))

def test_invalid_input_type():
    """Test that an error is raised for non-list inputs."""
    with pytest.raises(TypeError):
        merge_sort("not a list")
    
    with pytest.raises(TypeError):
        merge_sort(123)

def test_list_with_mixed_types():
    """Test sorting a list with comparable mixed types."""
    assert merge_sort([3, 1.5, 2, -1]) == [-1, 1.5, 2, 3]

def test_original_list_unchanged():
    """Verify that the original list remains unchanged."""
    original = [3, 1, 4, 1, 5, 9]
    sorted_list = merge_sort(original)
    assert original == [3, 1, 4, 1, 5, 9]
    assert sorted_list == [1, 1, 3, 4, 5, 9]