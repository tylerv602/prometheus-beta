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
    
    # Create sorted first column of the BWT matrix
    first_column = sorted(bwt)
    
    # Initialize tracking for reconstruction
    n = len(bwt)
    
    # Compute the 'next' array and character count
    next_array = [0] * n
    char_count = {}
    for i in range(n):
        char = bwt[i]
        if char not in char_count:
            char_count[char] = 0
        next_array[i] = char_count[char]
        char_count[char] += 1
    
    # Reconstruct the original string
    reconstructed = []
    current_index = bwt.index('$')
    
    for _ in range(n - 1):  # Exclude the terminator
        # Get next character from first column
        current_char = first_column[current_index]
        reconstructed.append(current_char)
        
        # Find the next index in the first column 
        current_index = first_column.index(current_char, 
                               first_column.count(current_char[:1]) - 
                               bwt.count(current_char) + 
                               bwt[:current_index].count(current_char))
    
    # Return the reconstructed string (note: could be reversed depending on rotation)
    return ''.join(reconstructed[::-1]).rstrip('$')