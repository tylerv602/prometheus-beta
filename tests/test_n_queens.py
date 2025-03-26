import pytest
from src.n_queens import solve_n_queens, count_n_queens_solutions

def test_solve_n_queens_1x1():
    """Test 1x1 board solution"""
    solutions = solve_n_queens(1)
    assert solutions == [['Q']]

def test_solve_n_queens_invalid_input():
    """Test invalid input raises ValueError"""
    with pytest.raises(ValueError):
        solve_n_queens(0)
    with pytest.raises(ValueError):
        solve_n_queens(-1)

def test_solve_n_queens_no_solution():
    """Test boards with no possible solutions"""
    assert solve_n_queens(2) is None
    assert solve_n_queens(3) is None

def test_solve_n_queens_4x4():
    """Test 4x4 board has solutions"""
    solutions = solve_n_queens(4)
    assert solutions is not None
    assert len(solutions) == 2  # 4x4 has 2 distinct solutions

def test_n_queens_solution_validation():
    """Validate that solutions meet N-Queens constraints"""
    def validate_solution(solution):
        # Convert solution to 2D board for easier checking
        board = [list(row) for row in solution]
        n = len(board)
        
        # Check queens
        queens = []
        for r in range(n):
            queen_col = board[r].index('Q')
            queens.append((r, queen_col))
        
        # Check no two queens threaten each other
        for i in range(len(queens)):
            for j in range(i+1, len(queens)):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                
                # Check column
                assert c1 != c2, f"Queens in same column at {queens[i]}, {queens[j]}"
                
                # Check diagonals
                assert abs(r1 - r2) != abs(c1 - c2), f"Queens on diagonal at {queens[i]}, {queens[j]}"
    
    # Test multiple board sizes
    for n in [4, 5, 6]:
        solutions = solve_n_queens(n)
        assert solutions is not None
        for solution in solutions:
            validate_solution(solution)

def test_count_n_queens_solutions():
    """Test solution counting for different board sizes"""
    # Known solution counts for different board sizes
    expected_counts = {
        1: 1,  # 1x1
        4: 2,  # 4x4
        5: 10,  # 5x5
        6: 4,  # 6x6
        7: 40,  # 7x7
        8: 92   # 8x8
    }
    
    for n, expected in expected_counts.items():
        assert count_n_queens_solutions(n) == expected

def test_count_n_queens_invalid_input():
    """Test invalid input for solution counting"""
    with pytest.raises(ValueError):
        count_n_queens_solutions(0)
    with pytest.raises(ValueError):
        count_n_queens_solutions(-1)