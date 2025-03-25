import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_zero_input():
    """Test that input 0 returns [0]"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_typical_cases():
    """Test several typical cases with known even-indexed sums"""
    test_cases = [
        # (input, expected subsequence)
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (3, [0, 1, 1, 2, 3]),
        (5, [0, 1, 1, 2, 3, 5]),
    ]
    
    for target_sum, expected in test_cases:
        subsequence = generate_fibonacci_subsequence(target_sum)
        
        # Validate sum of even-indexed elements
        assert sum(subsequence[::2]) == target_sum, f"Failed for input {target_sum}"
        
        # Validate Fibonacci property
        for i in range(2, len(subsequence)):
            assert subsequence[i] == subsequence[i-1] + subsequence[i-2], \
                f"Not a Fibonacci sequence for input {target_sum}"

def test_large_input():
    """Test a larger input that requires longer subsequence"""
    subsequence = generate_fibonacci_subsequence(21)
    assert sum(subsequence[::2]) == 21

def test_negative_input():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)

def test_impossible_input():
    """Test that extremely large inputs raise a ValueError"""
    with pytest.raises(ValueError, match="No Fibonacci subsequence found"):
        generate_fibonacci_subsequence(10**9)  # Extremely unlikely to find a match