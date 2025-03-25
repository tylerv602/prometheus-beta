import pytest
from src.count_anagrams import count_anagrams

def test_basic_anagram_count():
    """Test basic anagram counting scenarios"""
    assert count_anagrams('abab') == 4
    assert count_anagrams('abc') == 6
    assert count_anagrams('aa') == 1

def test_single_character():
    """Test single character input"""
    assert count_anagrams('a') == 1

def test_repeated_characters():
    """Test string with repeated characters"""
    assert count_anagrams('aaaa') == 1

def test_unique_characters():
    """Test string with all unique characters"""
    assert count_anagrams('abcde') == 15

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError"""
    with pytest.raises(ValueError):
        count_anagrams('')

def test_invalid_input_raises_error():
    """Test that input with non-lowercase letters raises a ValueError"""
    with pytest.raises(ValueError):
        count_anagrams('AbC')
    with pytest.raises(ValueError):
        count_anagrams('123')
    with pytest.raises(ValueError):
        count_anagrams('a1b')