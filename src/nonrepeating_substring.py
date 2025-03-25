def longest_nonrepeating_substring(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with no repeated characters
    
    Examples:
        >>> longest_nonrepeating_substring("abcabcbb")
        3
        >>> longest_nonrepeating_substring("bbbbb")
        1
        >>> longest_nonrepeating_substring("pwwkew")
        3
        >>> longest_nonrepeating_substring("")
        0
    """
    # Handle empty string edge case
    if not s:
        return 0
    
    # Use sliding window technique
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If character is already in set, remove characters from left 
        # until the repeating character is removed
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to set
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length