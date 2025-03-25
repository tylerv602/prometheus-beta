import pytest
import math
from src.circle_coverage import Circle, calculate_distance, do_circles_overlap, optimize_circle_coverage

def test_circle_initialization():
    """Test Circle class initialization."""
    circle = Circle(0, 0, 5)
    assert circle.x == 0
    assert circle.y == 0
    assert circle.radius == 5

def test_negative_radius_raises_error():
    """Test that negative radius raises a ValueError."""
    with pytest.raises(ValueError):
        Circle(0, 0, -1)

def test_calculate_distance():
    """Test distance calculation between circles."""
    circle1 = Circle(0, 0, 5)
    circle2 = Circle(3, 4, 2)
    
    expected_distance = 5  # sqrt(3^2 + 4^2)
    assert math.isclose(calculate_distance(circle1, circle2), expected_distance)

def test_circles_overlap():
    """Test circle overlap detection."""
    # Overlapping circles
    circle1 = Circle(0, 0, 5)
    circle2 = Circle(3, 0, 3)
    assert do_circles_overlap(circle1, circle2) is True
    
    # Non-overlapping circles
    circle3 = Circle(0, 0, 1)
    circle4 = Circle(10, 10, 1)
    assert do_circles_overlap(circle3, circle4) is False

def test_optimize_circle_coverage_single_circle():
    """Test optimization with a single circle."""
    circles = [Circle(0, 0, 5)]
    result = optimize_circle_coverage(circles)
    assert len(result) == 1
    assert result[0].x == 0
    assert result[0].y == 0
    assert result[0].radius == 5

def test_optimize_circle_coverage_multiple_circles():
    """Test optimization with multiple circles."""
    circles = [
        Circle(0, 0, 5),   # Large circle
        Circle(3, 0, 2),   # Smaller circle, overlapping with first
        Circle(10, 10, 3)  # Non-overlapping circle
    ]
    result = optimize_circle_coverage(circles)
    assert len(result) == 2  # Should reduce to 2 circles

def test_optimize_circle_coverage_empty_list():
    """Test that empty list raises an error."""
    with pytest.raises(ValueError):
        optimize_circle_coverage([])

def test_optimize_circle_coverage_no_overlap():
    """Test optimization with no overlapping circles."""
    circles = [
        Circle(0, 0, 2),
        Circle(10, 10, 3),
        Circle(-5, -5, 1)
    ]
    result = optimize_circle_coverage(circles)
    assert len(result) == 3  # All circles should be in the result