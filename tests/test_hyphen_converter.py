import pytest
from src.hyphen_converter import convert_hyphens_to_spaces

def test_convert_simple_hyphen():
    """Test converting a simple hyphenated string"""
    assert convert_hyphens_to_spaces('hello-world') == 'hello world'

def test_convert_multiple_hyphens():
    """Test converting a string with multiple hyphens"""
    assert convert_hyphens_to_spaces('convert-hyphens-to-spaces') == 'convert hyphens to spaces'

def test_convert_empty_string():
    """Test converting an empty string"""
    assert convert_hyphens_to_spaces('') == ''

def test_convert_no_hyphens():
    """Test a string with no hyphens"""
    assert convert_hyphens_to_spaces('hello') == 'hello'

def test_convert_multiple_consecutive_hyphens():
    """Test converting string with multiple consecutive hyphens"""
    assert convert_hyphens_to_spaces('hello----world') == 'hello    world'

def test_invalid_input_type():
    """Test raising TypeError for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_hyphens_to_spaces(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_hyphens_to_spaces(None)