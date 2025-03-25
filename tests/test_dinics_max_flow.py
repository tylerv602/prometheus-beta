import pytest
from src.dinics_max_flow import DinicMaxFlow

def test_simple_flow():
    """Test a simple flow network with a clear maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    
    dinics = DinicMaxFlow(graph)
    max_flow = dinics.max_flow(0, 5)
    assert max_flow == 19, f"Expected max flow of 19, got {max_flow}"

def test_complex_flow():
    """Test a more complex flow network with multiple paths."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 1, 3: 4},
        2: {3: 2, 4: 2},
        3: {4: 5, 5: 2},
        4: {5: 3},
        5: {}
    }
    
    dinics = DinicMaxFlow(graph)
    max_flow = dinics.max_flow(0, 5)
    assert max_flow == 5, f"Expected max flow of 5, got {max_flow}"

def test_no_flow_network():
    """Test a network with zero maximum flow."""
    graph = {
        0: {},
        1: {},
        2: {}
    }
    
    dinics = DinicMaxFlow(graph)
    max_flow = dinics.max_flow(0, 2)
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"

def test_same_source_sink():
    """Test when source and sink are the same node."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2},
        2: {}
    }
    
    dinics = DinicMaxFlow(graph)
    max_flow = dinics.max_flow(0, 0)
    assert max_flow == 0, f"Expected max flow of 0, got {max_flow}"

def test_invalid_nodes():
    """Test error handling for invalid source or sink nodes."""
    graph = {
        0: {1: 10},
        1: {}
    }
    
    dinics = DinicMaxFlow(graph)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        dinics.max_flow(2, 0)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        dinics.max_flow(0, 2)

def test_large_capacity_flow():
    """Test a network with large capacity edges."""
    graph = {
        0: {1: 1000, 2: 1000},
        1: {2: 500, 3: 400, 4: 600},
        2: {4: 900},
        3: {5: 1000},
        4: {3: 600, 5: 1000},
        5: {}
    }
    
    dinics = DinicMaxFlow(graph)
    max_flow = dinics.max_flow(0, 5)
    assert max_flow == 1400, f"Expected max flow of 1400, got {max_flow}"