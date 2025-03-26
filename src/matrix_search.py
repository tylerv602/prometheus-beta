def find_matrix_coordinates(matrix, target):
    """
    Find the coordinates (row, column) of a target value in a 2D matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, column) coordinates if found, or None if not found
    
    Raises:
        TypeError: If matrix is not a valid 2D list or target is of invalid type
        ValueError: If matrix is empty or contains inconsistent row lengths
    """
    # Validate input matrix
    if not isinstance(matrix, list):
        raise TypeError("Matrix must be a list")
    
    if not matrix:
        raise ValueError("Matrix must be a non-empty 2D list")
    
    # Check matrix consistency
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a 2D list")
    
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("All rows in the matrix must have the same length")
    
    # Search through the matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if value == target:
                return (row_idx, col_idx)
    
    # Return None if target not found
    return None