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

    # Use a dictionary to track counts and prevent overcounting
    num_counts = {}
    zero_sum_pairs = 0

    for num in arr:
        # Check if the negation of the current number exists
        if -num in num_counts and num_counts[-num] > 0:
            zero_sum_pairs += 1
            num_counts[-num] -= 1
        
        # Increment or initialize the count for the current number
        num_counts[num] = num_counts.get(num, 0) + 1

    return zero_sum_pairs