def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence.
    
    Returns:
        list: A Fibonacci subsequence satisfying the condition.
    
    Raises:
        ValueError: If no valid subsequence can be generated.
    """
    # Handle trivial cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return [0]
    
    # Try different maximum subsequence lengths
    for max_length in range(2, 50):  # Increased range to allow more complex subsequences
        for start_index in range(max_length):
            subsequence = []
            current_num = 0
            next_num = 1
            
            # Generate subsequence
            while len(subsequence) < max_length:
                subsequence.append(current_num)
                current_num, next_num = next_num, current_num + next_num
            
            # Slice the subsequence starting from different points
            for offset in range(start_index + 1):
                test_subsequence = subsequence[offset:offset+max_length]
                
                # Check even-indexed sum
                even_sum = sum(test_subsequence[::2])
                
                if even_sum == n:
                    return test_subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")