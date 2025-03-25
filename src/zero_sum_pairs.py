def count_zero_sum_pairs(arr):
    """
    Count the number of pairs of elements in the input array that sum to zero.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The number of pairs that sum up to zero.

    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")

    # Use a set for O(n) time complexity
    seen = set()
    zero_sum_pairs = 0

    for num in arr:
        # If the negation of the current number exists in seen, we found a zero-sum pair
        if -num in seen:
            zero_sum_pairs += 1
        # Add current number to seen set
        seen.add(num)

    return zero_sum_pairs