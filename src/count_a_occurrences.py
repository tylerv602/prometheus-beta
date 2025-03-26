def count_a_occurrences(input_string: str) -> int:
    """
    Count the number of 'a' characters in the input string, ignoring case sensitivity.

    Args:
        input_string (str): The string to search for 'a' occurrences.

    Returns:
        int: The number of 'a' characters in the string (case-insensitive).

    Examples:
        >>> count_a_occurrences("Apple")
        1
        >>> count_a_occurrences("banana")
        3
        >>> count_a_occurrences("")
        0
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.lower().count('a')