from typing import List
from collections import Counter

def count_anagrams(s: str) -> int:
    """
    Count the number of distinct anagrams in the given string.
    
    An anagram is a sequence of characters that can be rearranged to form another sequence.
    This function identifies and counts unique anagram configurations in the input string.
    
    Args:
        s (str): Input string containing only lowercase English letters
    
    Returns:
        int: Number of distinct anagrams found in the string
    
    Raises:
        ValueError: If the input string contains characters other than lowercase letters
    """
    # Validate input
    if not s or not all(c.islower() for c in s):
        raise ValueError("Input must be a non-empty string with only lowercase letters")
    
    # Track unique anagram signatures
    anagram_signatures = set()
    
    # Generate all possible substrings and their sorted representations
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            # Extract substring and create a canonical signature
            substring = s[start:start+length]
            # Create a string signature representing the character counts
            signature = ''.join(f'{char}{count}' for char, count in sorted(Counter(substring).items()))
            anagram_signatures.add(signature)
    
    return len(anagram_signatures)