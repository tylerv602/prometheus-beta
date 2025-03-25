"""
Tests for LZ78 Compression Algorithm
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_basic_compression_and_decompression():
    """Test basic string compression and decompression"""
    original = "TOBEORNOTTOBEORTOBE"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_single_character_string():
    """Test compression of a single character string"""
    original = "A"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_repeated_patterns():
    """Test string with repeated patterns"""
    original = "ABABABABAB"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError):
        lz78_compress("")

def test_non_string_input_raises_error():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        lz78_compress(123)
    with pytest.raises(TypeError):
        lz78_decompress(123)

def test_complex_string():
    """Test compression of a more complex string"""
    original = "the quick brown fox jumps over the lazy dog"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_unicode_string():
    """Test compression of a string with unicode characters"""
    original = "Hello, 世界! こんにちは"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_invalid_compressed_data():
    """Test that invalid compressed data raises ValueError"""
    with pytest.raises(ValueError):
        lz78_decompress([(1, 'a'), (10, 'b')])  # Non-sequential references

def test_compressed_data_type():
    """Test that invalid compressed data type raises TypeError"""
    with pytest.raises(TypeError):
        lz78_decompress("not a list")

def test_compression_efficiency():
    """Basic test to ensure some compression occurs"""
    original = "AAAAAAAAAAAAAAAAAAAA"
    compressed = lz78_compress(original)
    assert len(compressed) < len(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original