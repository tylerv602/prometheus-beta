def find_missing_number(nums):
    """
    Find the missing number in a list of integers from 1 to n.
    
    Args:
        nums (list): A list of unique integers from 1 to n with one number missing.
    
    Returns:
        int: The missing number in the sequence.
    
    Raises:
        ValueError: If the input list is empty or invalid.
        TypeError: If the input is not a list or contains non-integer elements.
    
    Examples:
        >>> find_missing_number([1, 3, 4, 5])
        2
        >>> find_missing_number([2, 3, 4, 5, 1])
        6
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All elements must be integers")
    
    # Calculate the expected sum of numbers from 1 to n
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given list
    actual_sum = sum(nums)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum