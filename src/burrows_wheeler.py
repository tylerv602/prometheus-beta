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
    
    # Length of the string
    n = len(bwt)
    
    # Create first column by sorting
    first_column = sorted(bwt)
    last_column = list(bwt)
    
    # Tracking character positions
    char_freq = {}
    for char in last_column:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Remap to track unique positions
    last_to_first = [0] * n
    char_counts = {}
    
    for i in range(n):
        char = last_column[i]
        if char not in char_counts:
            char_counts[char] = 0
        
        # Find position of this specific occurrence in first column
        current_freq = char_counts[char]
        current_char_instances = sum(1 for c in first_column[:first_column.index(char) + 1] if c == char)
        
        last_to_first[i] = first_column.index(char, current_char_instances - current_freq - 1)
        char_counts[char] += 1
    
    # Reconstruct original string
    result = []
    current_index = last_column.index('$')
    
    while len(result) < n - 1:
        # Get character from last column
        current_char = last_column[current_index]
        
        # Skip terminator
        if current_char == '$':
            current_index = (current_index + 1) % n
            continue
        
        # Append character
        result.append(current_char)
        
        # Move to next index
        current_index = last_to_first[current_index]
    
    # Return reconstructed string in original order
    return ''.join(result)