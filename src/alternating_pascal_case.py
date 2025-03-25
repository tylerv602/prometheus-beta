def to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    This function transforms an input string into alternating Pascal case, 
    where words are separated by an optional delimiter and each word 
    alternates between starting with an uppercase or lowercase letter.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    
    Examples:
        >>> to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_pascal_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the input string into words
    words = input_string.split()
    
    # Transform each word with alternating case
    alternating_words = []
    for word in words:
        transformed_word = ''.join(
            char.upper() if (i % 2 == 0) else char.lower() 
            for i, char in enumerate(word)
        )
        alternating_words.append(transformed_word)
    
    # Join the transformed words
    return ' '.join(alternating_words)