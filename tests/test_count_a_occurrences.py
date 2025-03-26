import pytest
from src.count_a_occurrences import count_a_occurrences

def test_count_a_occurrences_normal_cases():
    """Test various normal input scenarios."""
    assert count_a_occurrences("Apple") == 1
    assert count_a_occurrences("banana") == 3
    assert count_a_occurrences("APPLE") == 1
    assert count_a_occurrences("aAaA") == 4

def test_count_a_occurrences_edge_cases():
    """Test edge cases like empty string and no 'a's."""
    assert count_a_occurrences("") == 0
    assert count_a_occurrences("bcdefg") == 0

def test_count_a_occurrences_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_a_occurrences(123)
    with pytest.raises(TypeError):
        count_a_occurrences(None)

def test_count_a_occurrences_mixed_case():
    """Test strings with mixed case and multiple 'a' occurrences."""
    assert count_a_occurrences("AlAbAmA") == 4
    assert count_a_occurrences("AaAaAa") == 6