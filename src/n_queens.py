from typing import List, Optional

def solve_n_queens(n: int) -> Optional[List[List[str]]]:
    """
    Solve the N-Queens problem for a given board size.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        Optional[List[List[str]]]: A list of board configurations where each 
        board is represented as a list of strings. Each 'Q' represents a queen, 
        and '.' represents an empty square. Returns None if no solution exists.
    
    Raises:
        ValueError: If n is less than 1.
    """
    # Validate input
    if n < 1:
        raise ValueError("Board size must be at least 1")
    
    # Special case for 1x1 board
    if n == 1:
        return [['Q']]
    
    # Special cases where no solution exists
    if n == 2 or n == 3:
        return None
    
    def is_safe(board: List[int], row: int, col: int) -> bool:
        """
        Check if a queen can be placed on board at the given row and column.
        
        Args:
            board (List[int]): Current board configuration (column positions of queens)
            row (int): Row to place the queen
            col (int): Column to place the queen
        
        Returns:
            bool: True if queen can be placed safely, False otherwise
        """
        # Check columns and diagonals
        for r in range(row):
            # Check if queens in previous rows attack this position
            if (board[r] == col or  # Same column
                board[r] - r == col - row or  # Diagonal (top-left to bottom-right)
                board[r] + r == col + row):  # Diagonal (top-right to bottom-left)
                return False
        return True
    
    def solve(board: List[int], row: int) -> List[List[str]]:
        """
        Recursive backtracking solver for N-Queens problem.
        
        Args:
            board (List[int]): Current board configuration
            row (int): Current row being processed
        
        Returns:
            List[List[str]]: List of valid board configurations
        """
        # Base case: all queens are placed
        if row == n:
            # Convert integer board representation to string representation
            result = []
            for r in range(n):
                row_str = ['.' * board[r] + 'Q' + '.' * (n - board[r] - 1)]
                result.append(row_str[0])
            return [result]
        
        solutions = []
        # Try placing queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                # Place queen and recurse
                board[row] = col
                solutions.extend(solve(board, row + 1))
        
        return solutions
    
    # Initialize board and solve
    board = [0] * n
    return solve(board, 0) or None

def count_n_queens_solutions(n: int) -> int:
    """
    Count the number of possible solutions for the N-Queens problem.
    
    Args:
        n (int): The size of the chessboard and number of queens to place.
    
    Returns:
        int: Number of unique solutions
    
    Raises:
        ValueError: If n is less than 1.
    """
    solutions = solve_n_queens(n)
    return len(solutions) if solutions else 0