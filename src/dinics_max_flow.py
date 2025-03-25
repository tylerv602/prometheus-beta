from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    """
    Implementation of Dinic's algorithm for maximum flow.
    
    Dinic's algorithm is an efficient algorithm for computing the maximum flow 
    in a flow network using a combination of breadth-first search and depth-first search.
    
    Time Complexity: O(V^2 * E)
    Space Complexity: O(V + E)
    """
    
    def __init__(self, graph: Dict[int, Dict[int, int]]):
        """
        Initialize the Dinic's max flow algorithm.
        
        :param graph: Adjacency list representation of the graph 
                     where graph[u][v] represents the capacity from u to v
        """
        self.graph = graph
        # Get all unique nodes
        self.nodes = set()
        for u in graph:
            self.nodes.add(u)
            for v in graph[u]:
                self.nodes.add(v)
        
    def _bfs(self, source: int, sink: int) -> List[int]:
        """
        Breadth-first search to build level graph and check reachability.
        
        :param source: Source node
        :param sink: Sink node
        :return: List of levels for each node, or None if sink is unreachable
        """
        # Initialize level and visited tracking
        level = {node: -1 for node in self.nodes}
        level[source] = 0
        
        # Queue for BFS
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            # Check all adjacent nodes
            for v, capacity in self.graph.get(u, {}).items():
                # Only proceed if not visited and capacity > 0
                if level[v] == -1 and capacity > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        # Return None if sink is unreachable
        return level if level[sink] != -1 else None
    
    def _dfs(self, u: int, sink: int, flow: int, level: Dict[int, int], 
             flow_graph: Dict[int, Dict[int, int]]) -> int:
        """
        Depth-first search to find augmenting paths.
        
        :param u: Current node
        :param sink: Sink node
        :param flow: Current flow
        :param level: Level graph from BFS
        :param flow_graph: Residual graph tracking flows
        :return: Maximum additional flow
        """
        # Reached sink, return current flow
        if u == sink:
            return flow
        
        # Try all adjacent nodes
        for v, capacity in self.graph.get(u, {}).items():
            # Check residual capacity and level condition
            residual_capacity = capacity - flow_graph.get(u, {}).get(v, 0)
            if residual_capacity > 0 and level[v] == level[u] + 1:
                # Recursively find possible flow
                curr_flow = min(flow, residual_capacity)
                temp_flow = self._dfs(v, sink, curr_flow, level, flow_graph)
                
                # If flow found, update flow graph
                if temp_flow > 0:
                    # Update forward and backward edges
                    flow_graph.setdefault(u, {})[v] = flow_graph.get(u, {}).get(v, 0) + temp_flow
                    flow_graph.setdefault(v, {})[u] = flow_graph.get(v, {}).get(u, 0) - temp_flow
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink.
        
        :param source: Source node
        :param sink: Sink node
        :return: Maximum flow value
        :raises ValueError: If source or sink not in graph
        """
        # Validate source and sink
        if source not in self.nodes or sink not in self.nodes:
            raise ValueError("Source or sink node not in graph")
        
        # Check for same source and sink
        if source == sink:
            return 0
        
        # Initialize flow tracking
        max_flow = 0
        flow_graph = {}
        
        # Repeat until no augmenting path exists
        while True:
            # Build level graph via BFS
            level = self._bfs(source, sink)
            
            # No path exists, we're done
            if not level:
                break
            
            # Find max flow via DFS
            while True:
                # Try to find augmenting path
                path_flow = self._dfs(source, sink, float('inf'), level, flow_graph)
                
                # No more augmenting paths
                if path_flow == 0:
                    break
                
                # Add to total max flow
                max_flow += path_flow
        
        return max_flow