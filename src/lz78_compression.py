"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based lossless compression algorithm that builds 
a dynamic dictionary of encountered sequences during compression.
"""

def lz78_compress(input_data):
    """
    Compress input data using the LZ78 compression algorithm.
    
    Args:
        input_data (str): The input string to be compressed.
    
    Returns:
        list: A list of tuples representing compressed data.
              Each tuple is of the form (index, character).
              Index 0 represents a new sequence, 
              non-zero index references a previously seen sequence.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_data, str):
        raise TypeError("Input must be a string")
    
    if not input_data:
        raise ValueError("Input cannot be an empty string")
    
    # Initialize dictionary and output
    dictionary = {0: ''}  # 0 represents empty string
    current_code = 1
    compressed = []
    
    # Current matched sequence
    current_sequence = ''
    
    # Compress the input
    for char in input_data:
        # Try to extend current sequence
        test_sequence = current_sequence + char
        
        # Check if this sequence is in the dictionary
        found = False
        for code, sequence in dictionary.items():
            if sequence == test_sequence:
                current_sequence = test_sequence
                found = True
                break
        
        # If sequence not found, add to compressed output and dictionary
        if not found:
            # Find the code for the current sequence
            current_code_index = 0
            for code, sequence in dictionary.items():
                if sequence == current_sequence:
                    current_code_index = code
                    break
            
            # Add to compressed output and dictionary
            compressed.append((current_code_index, char))
            dictionary[current_code] = test_sequence
            current_code += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle any remaining sequence
    if current_sequence:
        for code, sequence in dictionary.items():
            if sequence == current_sequence:
                compressed.append((code, ''))
                break
    
    return compressed

def lz78_decompress(compressed_data):
    """
    Decompress data compressed using the LZ78 algorithm.
    
    Args:
        compressed_data (list): List of tuples from LZ78 compression.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list of tuples.
        ValueError: If input tuples are invalid.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    # Initialize dictionary and output
    dictionary = {0: ''}
    current_code = 1
    decompressed = []
    
    # Decompress the input
    for index, char in compressed_data:
        # Validate input tuple
        if not isinstance(index, int) or not isinstance(char, str):
            raise ValueError(f"Invalid compressed data tuple: {(index, char)}")
        
        # Retrieve the referenced sequence
        if index not in dictionary:
            raise ValueError(f"Invalid dictionary reference: {index}")
        
        # Build the current sequence
        current_sequence = dictionary[index] + char
        decompressed.append(current_sequence)
        
        # Add to dictionary
        dictionary[current_code] = current_sequence
        current_code += 1
    
    # Return the full decompressed string
    return ''.join(decompressed)