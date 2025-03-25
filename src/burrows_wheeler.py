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
    
    # Find the index of the original string
    original_index = sorted_rotations.index(text_with_terminator)
    
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
    
    # Get the length of the string
    n = len(bwt)
    
    # Create first column by sorting last column
    first_column = sorted(bwt)
    
    # Create mapping for tracking character positions
    last_to_first = {}
    for i, char in enumerate(first_column):
        if char not in last_to_first:
            last_to_first[char] = i
    
    # Reconstruct the original string
    result = []
    current_char = '$'
    
    for _ in range(n - 1):  # Exclude the terminator
        # Find index of current character in last column
        current_index = bwt.index(current_char)
        
        # Move to the next character in the first column
        current_char = first_column[current_index]
        result.append(current_char)
    
    # Reverse the result to get the original string
    return ''.join(result[::-1]).rstrip('$')