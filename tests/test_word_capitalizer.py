import pytest
from src.word_capitalizer import capitalize_words

def test_capitalize_normal_string():
    """Test capitalizing a normal string with multiple words."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_already_capitalized():
    """Test string that is already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_mixed_case():
    """Test string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_capitalize_empty_string():
    """Test empty string input."""
    assert capitalize_words("") == ""

def test_capitalize_single_word():
    """Test single word input."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_with_extra_spaces():
    """Test string with extra spaces."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_invalid_input():
    """Test non-string input raises TypeError."""
    with pytest.raises(TypeError):
        capitalize_words(123)
    with pytest.raises(TypeError):
        capitalize_words(None)