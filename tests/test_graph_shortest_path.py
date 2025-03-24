import pytest
from src.graph_shortest_path import find_shortest_path


def test_basic_path_exists():
    """Test finding a path between two connected nodes"""
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }
    path = find_shortest_path(graph, 1, 5)
    assert path is not None
    assert path == [1, 2, 4, 5] or path == [1, 3, 4, 5]


def test_same_node_path():
    """Test path when start and end nodes are the same"""
    graph = {
        1: [2],
        2: [1]
    }
    path = find_shortest_path(graph, 1, 1)
    assert path == [1]


def test_no_path_exists():
    """Test case when no path exists between nodes"""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    path = find_shortest_path(graph, 1, 4)
    assert path is None


def test_node_not_in_graph():
    """Test handling of nodes not in the graph"""
    graph = {
        1: [2],
        2: [1]
    }
    with pytest.raises(ValueError):
        find_shortest_path(graph, 1, 3)
    
    with pytest.raises(ValueError):
        find_shortest_path(graph, 3, 1)


def test_complex_path():
    """Test finding path in a more complex graph"""
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    path = find_shortest_path(graph, 1, 6)
    assert path is not None
    assert path in ([1, 3, 6], [1, 2, 5, 6])


def test_multiple_paths():
    """Test when multiple paths exist, returns shortest"""
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [5],
        5: []
    }
    path = find_shortest_path(graph, 1, 5)
    assert path is not None
    assert len(path) == 3  # Ensure shortest path is returned
    assert path in ([1, 2, 5], [1, 3, 4, 5])