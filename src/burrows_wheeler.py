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
    
    # Add a special terminator character to ensure unique rotation
    text_with_terminator = text + '$'
    
    # Generate all rotations of the input string
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation to form BWT
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt

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
    
    # Create first and last column for reconstruction
    n = len(bwt)
    
    # Create first column and last column
    first_column = sorted(bwt)
    last_column = list(bwt)
    
    # Count of each character in the first column
    char_count = {}
    for c in first_column:
        char_count[c] = char_count.get(c, 0) + 1
    
    # Create next array to track character ordering
    next_array = [0] * n
    char_position = {c: 0 for c in set(first_column)}
    
    for i in range(n):
        char = last_column[i]
        next_array[i] = char_position[char]
        char_position[char] += 1
    
    # Reconstruct the original string
    result = []
    current_index = last_column.index('$')
    
    for _ in range(n - 1):  # Exclude the terminator
        result.append(last_column[current_index])
        current_index = next_array[current_index]
    
    # Reverse and join the result
    return ''.join(result[::-1])