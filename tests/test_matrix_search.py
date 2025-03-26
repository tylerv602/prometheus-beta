import pytest
from src.matrix_search import find_matrix_coordinates

def test_find_matrix_coordinates_basic():
    """Test basic matrix coordinate search"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)

def test_find_matrix_coordinates_not_found():
    """Test when target is not in the matrix"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_find_matrix_coordinates_error_handling():
    """Test various error conditions"""
    # Empty matrix
    with pytest.raises(ValueError, match="Matrix must be a non-empty 2D list"):
        find_matrix_coordinates([], 5)
    
    # Not a list
    with pytest.raises(TypeError):
        find_matrix_coordinates("not a matrix", 5)
    
    # Inconsistent row lengths
    with pytest.raises(ValueError, match="All rows in the matrix must have the same length"):
        find_matrix_coordinates([[1, 2], [3, 4, 5]], 5)

def test_find_matrix_coordinates_edge_cases():
    """Test edge cases like single-element matrix"""
    # Single element matrix
    matrix = [[42]]
    assert find_matrix_coordinates(matrix, 42) == (0, 0)
    assert find_matrix_coordinates(matrix, 43) is None
    
    # Large matrix
    large_matrix = [[i*10 + j for j in range(10)] for i in range(10)]
    assert find_matrix_coordinates(large_matrix, 42) == (4, 2)

def test_find_matrix_coordinates_first_occurrence():
    """Ensure function returns first occurrence of target"""
    matrix = [
        [1, 2, 1],
        [1, 2, 3],
        [4, 1, 5]
    ]
    assert find_matrix_coordinates(matrix, 1) == (0, 0)