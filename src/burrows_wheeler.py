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
    
    # Sort the characters to create first column
    first_column = sorted(bwt)
    
    # Create a mapping to track the order of characters
    next_char = {}
    for i, char in enumerate(bwt):
        if char not in next_char:
            next_char[char] = 0
        next_char[char] += 1
    
    # Reconstruct the original string
    reconstructed = [''] * n
    current_char = '$'  # Start with terminator
    for i in range(n - 1, -1, -1):
        # Find the index of current character in the first column
        current_index = first_column.index(current_char)
        
        # Adjust for multiple occurrences
        current_index = next_char[current_char] - 1
        next_char[current_char] -= 1
        
        # Add character to reconstruction
        reconstructed[i] = current_char
        
        # Move to next character using last column (BWT)
        current_char = bwt[current_index]
    
    # Remove terminator and join
    original = ''.join(reconstructed).rstrip('$')
    
    return original