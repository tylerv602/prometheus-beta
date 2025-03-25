import pytest
from src.nonrepeating_substring import longest_nonrepeating_substring

def test_basic_scenarios():
    # Standard scenarios
    assert longest_nonrepeating_substring("abcabcbb") == 3  # "abc"
    assert longest_nonrepeating_substring("bbbbb") == 1     # "b"
    assert longest_nonrepeating_substring("pwwkew") == 3    # "wke"

def test_edge_cases():
    # Empty string
    assert longest_nonrepeating_substring("") == 0
    
    # Single character
    assert longest_nonrepeating_substring("a") == 1
    
    # All unique characters
    assert longest_nonrepeating_substring("abcdef") == 6

def test_complex_scenarios():
    # Mixed character scenarios
    assert longest_nonrepeating_substring("dvdf") == 3
    assert longest_nonrepeating_substring("tmmzuxt") == 5

def test_repeated_characters():
    # Scenarios with repeated characters in different positions
    assert longest_nonrepeating_substring("abba") == 2
    assert longest_nonrepeating_substring("aab") == 2
    assert longest_nonrepeating_substring("aabcde") == 5

def test_unicode_characters():
    # Test with unicode characters
    assert longest_nonrepeating_substring("🌈🌞🌈") == 2
    assert longest_nonrepeating_substring("résumé") == 5