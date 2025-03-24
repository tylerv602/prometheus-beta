import pytest
from src.count_occurrences import count_element_occurrences

def test_count_occurrences_basic():
    """Test basic counting of element occurrences."""
    assert count_element_occurrences([1, 2, 3, 2, 2], 2) == 3

def test_count_occurrences_empty_list():
    """Test counting in an empty list."""
    assert count_element_occurrences([], 5) == 0

def test_count_occurrences_no_matches():
    """Test when element is not in the list."""
    assert count_element_occurrences([1, 2, 3, 4], 5) == 0

def test_count_occurrences_mixed_types():
    """Test counting with mixed type list."""
    assert count_element_occurrences([1, 'a', 1, 'a', 1], 1) == 3

def test_count_occurrences_invalid_input():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences("not a list", 1)

def test_count_occurrences_none():
    """Test counting None occurrences."""
    assert count_element_occurrences([None, 1, None, 2], None) == 2