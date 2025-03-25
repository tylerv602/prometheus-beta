import pytest
from src.find_pairs_sum_to_target import find_pairs_sum_to_target

def test_basic_pairs():
    """Test finding pairs that sum to target"""
    assert set(find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)) == {(2, 5), (3, 4)}

def test_multiple_occurrences():
    """Test handling lists with duplicate numbers"""
    assert set(find_pairs_sum_to_target([1, 1, 2, 3, 4, 5], 6)) == {(1, 5), (2, 4)}

def test_empty_list():
    """Test with an empty list"""
    assert find_pairs_sum_to_target([], 5) == []

def test_no_pairs():
    """Test when no pairs sum to target"""
    assert find_pairs_sum_to_target([1, 2, 3, 4], 10) == []

def test_negative_numbers():
    """Test with negative numbers"""
    assert set(find_pairs_sum_to_target([-1, 0, 1, 2, -2, 3], 1)) == {(-1, 2), (0, 1)}

def test_repeated_pairs():
    """Test handling lists with repeated numbers"""
    assert set(find_pairs_sum_to_target([2, 2, 2, 2], 4)) == {(2, 2)}

def test_zero_target():
    """Test with zero as target"""
    assert set(find_pairs_sum_to_target([-1, 0, 1, 2, -2], 0)) == {(-2, 2), (-1, 1)}

def test_large_numbers():
    """Test with large numbers"""
    assert set(find_pairs_sum_to_target([1000000, -1000000, 500000, -500000], 0)) == {(-1000000, 1000000), (-500000, 500000)}

def test_sorted_output():
    """Verify that output pairs are sorted"""
    result = find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)
    assert result == [(2, 5), (3, 4)]