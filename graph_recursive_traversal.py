from collections import defaultdict

class Graph:
    """Graph Implementation
    
    Graph is stored using an adjacency list.
    Contains methods associated with graph (add_node, depth_first, breadth_first).
    Traversals are coded recursively.
    
    Attributes:
        _graph (:obj:`dict`): Stores the graph as an adjacency list
        _root: Pointer pointing to root node of graph
    """
    def __init__(self, root: str):
        """Initialise Graph

        Args:
            root (str): Root (default) node of graph
        """
        self._graph = defaultdict(list)
        self._root = root
            
    def add_node(self, value: str, edges: list):
        """Add Node method

        Adds a node and its edges to a graph

        Args:
            value (str): Value stored in the node
            edges (list): Edges linked to the node in the graph
        """
        self._graph[value] += edges
    
    def depth_first(self, visited: list = None, current_node: str = None) -> list:
        """DFT method

        Args:
            visited (list, optional): Keeps track of all visited nodes during recursion. Defaults to None.
            current_node (str, optional): The node that the current frame of the function is handling. Defaults to None.

        Returns:
            list: The order of traversal in DFT
        """
        # Default arguments if `None`
        if current_node is None:
            current_node = self._root
        if visited is None:
            visited = []
        
        # Add current node to list of visited nodes
        visited.append(current_node)
        
        # Find unvisited edges and traverse through them
        for edge in self._graph[current_node]:
            if edge not in visited:
                self.depth_first(visited, edge)
        
        return visited
    
    def breadth_first(self, queue: list = None, visited: list = None, current_node: str = None) -> list:
        """BFT method

        Args:
            queue (list, optional): Stores order of nodes, on which BFT method will be called sequentially. Defaults to None.
            visited (list, optional): Keeps track of all visited nodes during recursion. Defaults to None.
            current_node (str, optional): The node that the current frame of the function is handling. Defaults to None.

        Returns:
            list: [description]
        """
        # Default arguments if `None`
        if visited is None:
            visited = []
        if current_node is None:
            current_node = self._root
        if queue is None:
            queue = []
        
        # Add current node to list of visited nodes
        visited.append(current_node)
        
        # Find unvisited edges and add them to end of queue
        for edge in self._graph[current_node]:
            if edge not in visited and edge not in queue:
                queue.append(edge)
        
        # BFT through first element in queue and remove that element
        if queue:
            self.breadth_first(queue, visited, queue.pop(0))
            
        return visited
   
def main():
    """Main function
    
    Test class `Graph`
    """
    
    # Create graph and add nodes
    my_graph = Graph('A')
    adjacency_list = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['C'],
        'E': ['A', 'C', 'D', 'F'],
        'F': ['B', 'D', 'E']
    }
    for key in adjacency_list.keys():
        my_graph.add_node(key, adjacency_list[key])
    
    # DFT - nodes 'A' and 'B'    
    print(f"DFT Root: A, Traversal: {my_graph.depth_first()}")
    print(f"DFT Root: D, Traversal: {my_graph.depth_first(current_node='D')}")
    
    # BFT - nodes 'A' and 'D'
    print(f"BFT Root: A, Traversal: {my_graph.breadth_first()}")
    print(f"BFT Root: D, Traversal: {my_graph.breadth_first(current_node='D')}")

if __name__ == "__main__":
    main()