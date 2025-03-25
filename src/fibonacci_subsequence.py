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
    
    # Try different subsequence lengths
    for length in range(2, 20):  # Reasonable upper limit to prevent infinite loop
        # Generate potential subsequence
        subsequence = [0, 1]
        
        # Extend the subsequence
        while len(subsequence) < length:
            subsequence.append(subsequence[-1] + subsequence[-2])
        
        # Check even-indexed sum
        even_sum = sum(subsequence[::2])
        
        if even_sum == n:
            return subsequence
    
    # If no subsequence found
    raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")