import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_fibonacci_subsequence_zero_length():
    """Test generating a Fibonacci subsequence of length 0."""
    assert generate_fibonacci_subsequence(0) == []

def test_fibonacci_subsequence_length_one():
    """Test generating a Fibonacci subsequence of length 1."""
    assert generate_fibonacci_subsequence(1) == [0]

def test_fibonacci_subsequence_length_two():
    """Test generating a Fibonacci subsequence of length 2."""
    assert generate_fibonacci_subsequence(2) == [0, 1]

def test_fibonacci_subsequence_length_five():
    """Test generating a Fibonacci subsequence of length 5."""
    assert generate_fibonacci_subsequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_subsequence_length_ten():
    """Test generating a Fibonacci subsequence of length 10."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert generate_fibonacci_subsequence(10) == expected

def test_invalid_input_negative_length():
    """Test that a negative length raises a ValueError."""
    with pytest.raises(ValueError, match="Length of subsequence must be non-negative"):
        generate_fibonacci_subsequence(-1)

def test_invalid_input_non_integer():
    """Test that a non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_fibonacci_subsequence(None)