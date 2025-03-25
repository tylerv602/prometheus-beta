import pytest
from src.vowel_counter import count_vowels

def test_count_vowels_basic():
    """Test basic vowel counting functionality."""
    assert count_vowels("hello") == 2
    assert count_vowels("WORLD") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("xyz") == 0

def test_count_vowels_mixed_case():
    """Test case-insensitive vowel counting."""
    assert count_vowels("AeIoU") == 5
    assert count_vowels("PytHOn") == 1

def test_count_vowels_empty_string():
    """Test counting vowels in an empty string."""
    assert count_vowels("") == 0

def test_count_vowels_special_characters():
    """Test counting vowels with special characters and spaces."""
    assert count_vowels("Hello, World!") == 3
    assert count_vowels("123 a b c") == 1

def test_count_vowels_multiple_words():
    """Test counting vowels in multiple words."""
    assert count_vowels("The quick brown fox") == 5