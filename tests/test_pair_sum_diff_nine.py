import os
import pytest
from src.pair_sum_diff_nine import sum_pairs_with_diff_nine

def test_basic_pairs():
    # Create a test file with basic pairs
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\n5\n14\n20\n29\n")
    
    # Expected pairs: (1,10), (5,14), (20,29)
    # Sum of these pairs: (1+10) + (5+14) + (20+29) = 11 + 19 + 49 = 79
    assert sum_pairs_with_diff_nine('tests/test_numbers.txt') == 79

def test_no_pairs():
    # Create a file with no valid pairs
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n2\n3\n4\n5\n")
    
    assert sum_pairs_with_diff_nine('tests/test_numbers.txt') == 0

def test_repeated_pairs():
    # Create a file with multiple ways to form pairs
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\n1\n10\n")
    
    # Pairs: (1,10), (1,10)
    # Sum: (1+10) + (1+10) = 11 + 11 = 22
    assert sum_pairs_with_diff_nine('tests/test_numbers.txt') == 22

def test_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        sum_pairs_with_diff_nine('non_existent_file.txt')

def test_invalid_number_format():
    # Create a file with invalid number
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("1\n10\nabc\n")
    
    # Test that invalid format raises ValueError
    with pytest.raises(ValueError):
        sum_pairs_with_diff_nine('tests/test_numbers.txt')

def test_empty_file():
    # Create an empty file
    with open('tests/test_numbers.txt', 'w') as f:
        f.write("")
    
    # Should return 0 for an empty file
    assert sum_pairs_with_diff_nine('tests/test_numbers.txt') == 0

# Clean up test file after tests
def teardown_module(module):
    try:
        os.remove('tests/test_numbers.txt')
    except FileNotFoundError:
        pass