import pytest
from src.sentence_case import to_sentence_case

def test_basic_sentence_case():
    """Test conversion of basic strings to sentence case."""
    assert to_sentence_case("hello world") == "Hello world"
    assert to_sentence_case("HELLO WORLD") == "Hello world"
    assert to_sentence_case("hello WORLD") == "Hello world"

def test_mixed_case():
    """Test conversion of mixed case strings."""
    assert to_sentence_case("hElLo WoRlD") == "Hello world"

def test_empty_string():
    """Test handling of empty string."""
    assert to_sentence_case("") == ""

def test_single_character():
    """Test conversion of single character strings."""
    assert to_sentence_case("a") == "A"
    assert to_sentence_case("Z") == "Z"

def test_string_with_numbers():
    """Test conversion of strings with numbers."""
    assert to_sentence_case("hello 123 world") == "Hello 123 world"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_sentence_case(123)
    
    with pytest.raises(TypeError):
        to_sentence_case(None)
    
    with pytest.raises(TypeError):
        to_sentence_case(["hello"])