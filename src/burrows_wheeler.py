def burrows_wheeler_transform(text):
    """
    Implement the Burrows-Wheeler Transform for data compression.
    
    Args:
        text (str): Input string to be transformed
    
    Returns:
        str: Burrows-Wheeler transformed string
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        raise ValueError("Input string cannot be empty")
    
    # Generate all rotations by adding a unique terminator
    text_with_terminator = text + '$'
    
    # Compute all rotations
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort rotations and get last characters
    sorted_rotations = sorted(rotations)
    
    # BWT is the last characters of sorted lexicographically
    return ''.join(rotation[-1] for rotation in sorted_rotations)

def inverse_burrows_wheeler_transform(bwt):
    """
    Implement the inverse Burrows-Wheeler Transform.
    
    Args:
        bwt (str): Burrows-Wheeler transformed string
    
    Returns:
        str: Original text before transformation
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    """
    # Validate input
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string")
    
    if not bwt:
        raise ValueError("Input string cannot be empty")
    
    # Remove terminator if present
    bwt = bwt.replace('$', '')
    
    # Compute first column by sorting
    first_column = sorted(bwt)
    last_column = list(bwt)
    
    # Reconstruct transform
    n = len(last_column)
    result = []
    
    # Start with first occurrence (lexicographically smallest)
    current_index = last_column.index(min(last_column))
    
    for _ in range(n):
        # Get current character
        result.append(last_column[current_index])
        
        # Find next index in first column
        current_index = first_column.index(last_column[current_index])
    
    return ''.join(result[:n])