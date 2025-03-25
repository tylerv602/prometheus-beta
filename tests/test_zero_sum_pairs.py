import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_basic_zero_sum_pairs():
    """Test basic scenarios of zero-sum pairs."""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2
    assert count_zero_sum_pairs([]) == 0
    assert count_zero_sum_pairs([0, 0, 0]) == 1

def test_multiple_same_pair():
    """Test cases with multiple instances of the same zero-sum pair."""
    assert count_zero_sum_pairs([1, -1, 1, -1]) == 2

def test_zero_sum_with_zero():
    """Test scenarios involving zero."""
    assert count_zero_sum_pairs([0, 0, 0, 1, -1]) == 2

def test_negative_cases():
    """Test scenarios with no zero-sum pairs."""
    assert count_zero_sum_pairs([1, 2, 3, 4, 5]) == 0
    assert count_zero_sum_pairs([-1, -2, -3]) == 0

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_zero_sum_pairs("not a list")
    with pytest.raises(TypeError):
        count_zero_sum_pairs(123)
    with pytest.raises(TypeError):
        count_zero_sum_pairs(None)