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
    
    # Add a unique terminator
    text_with_terminator = text + '$'
    
    # Create rotations
    rotations = [text_with_terminator[i:] + text_with_terminator[:i] 
                 for i in range(len(text_with_terminator))]
    
    # Sort rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # BWT is last characters of sorted rotations
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
    
    # Ensure terminator is present
    if '$' not in bwt:
        bwt += '$'
    
    # Create sorted first column
    first_column = sorted(bwt)
    last_column = list(bwt)
    
    # Track character counts
    char_counts = {}
    for char in first_column:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Create next indices for reconstruction
    next_indices = [0] * len(last_column)
    current_counts = {}
    
    for i, char in enumerate(last_column):
        current_counts[char] = current_counts.get(char, 0) + 1
        next_indices[i] = current_counts[char] - 1
    
    # Reconstruct
    result = []
    current_index = last_column.index('$')
    
    while len(result) < len(last_column) - 1:
        # Get character from last column
        current_char = last_column[current_index]
        
        # Skip terminator
        if current_char == '$':
            current_index = (current_index + 1) % len(last_column)
            continue
        
        # Add to result
        result.append(current_char)
        
        # Find next index in first column
        current_index = first_column.index(current_char, 
                               first_column.count(current_char[:1]) - 
                               last_column.count(current_char) + 
                               last_column[:current_index].count(current_char))
    
    # Return reconstructed text (reversed)
    return ''.join(result[::-1])