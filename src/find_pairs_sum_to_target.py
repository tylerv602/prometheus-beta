def find_pairs_sum_to_target(numbers, target):
    """
    Find unique pairs of numbers in a list that sum to the target value.

    Args:
        numbers (list): A list of integers to search for pairs.
        target (int): The target sum to find pairs for.

    Returns:
        list: A list of unique pairs (as tuples) that sum to the target.
              Pairs are sorted in ascending order with no duplicates.

    Examples:
        >>> find_pairs_sum_to_target([1, 2, 3, 4, 5], 7)
        [(2, 5), (3, 4)]
        >>> find_pairs_sum_to_target([1, 1, 2, 3, 4, 5], 6)
        [(1, 5), (2, 4)]

    Notes:
        - Time complexity: O(n)
        - Space complexity: O(n)
    """
    # Handle empty or None input
    if not numbers:
        return []

    # Use a dictionary to track occurrences and avoid duplicate pairs
    num_dict = {}
    unique_pairs = set()

    for num in numbers:
        complement = target - num
        
        # If complement exists in the dictionary and hasn't been used
        if complement in num_dict and num_dict[complement] > 0:
            # Create a sorted pair to avoid duplicates
            pair = tuple(sorted((num, complement)))
            unique_pairs.add(pair)
        
        # Track the occurrence of the current number
        num_dict[num] = num_dict.get(num, 0) + 1

    # Remove used numbers to prevent duplicate pairs
    for pair in unique_pairs:
        num_dict[pair[0]] -= 1
        num_dict[pair[1]] -= 1

    # Convert to sorted list for consistent output
    return sorted(list(unique_pairs))