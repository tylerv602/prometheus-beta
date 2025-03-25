def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string case-insensitively.

    Args:
        text (str): The input string to count vowels in.

    Returns:
        int: The total number of vowels (a, e, i, o, u) in the text.

    Examples:
        >>> count_vowels("Hello")
        2
        >>> count_vowels("PYTHON")
        1
        >>> count_vowels("aEiOu")
        5
        >>> count_vowels("")
        0
    """
    # Convert the text to lowercase to make the count case-insensitive
    text = text.lower()
    
    # Define the set of vowels to check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Count the number of vowels in the text
    return sum(1 for char in text if char in vowels)