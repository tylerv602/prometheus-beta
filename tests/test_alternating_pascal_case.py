import pytest
from src.alternating_pascal_case import to_alternating_pascal_case

def test_basic_conversion():
    """Test basic string conversion to alternating Pascal case."""
    assert to_alternating_pascal_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_pascal_case("python programming") == "PyThOn PrOgRaMmInG"

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_pascal_case("hello") == "HeLlO"
    assert to_alternating_pascal_case("WORLD") == "WoRlD"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert to_alternating_pascal_case("test multiple words") == "TeSt MuLtIpLe WoRdS"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_pascal_case("MiXeD CaSe InPuT") == "MiXeD CaSe InPuT"

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_pascal_case(123)
    
    # Test empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        to_alternating_pascal_case("")

def test_special_characters():
    """Test conversion with special characters and mixed inputs."""
    assert to_alternating_pascal_case("hello! world?") == "HeLlO! WoRlD?"
    assert to_alternating_pascal_case("123 abc") == "123 AbC"