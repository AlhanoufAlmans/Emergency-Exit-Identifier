from Graph import Graph
import math
import Execute as Ex

# Create graph
graph = Graph()

# Add nodes to graph
graph.add_node(0, 'A', (35, 50), 0)
graph.add_node(math.inf, 'C', (25, 48), 6)
graph.add_node(math.inf, 'E', (65, 35), 25)
graph.add_node(math.inf, 'H', (60, 20), 11)
graph.add_node(math.inf, 'J', (30, 35), 11)
graph.add_node(math.inf, 'K', (25, 20), 3)
graph.add_node(math.inf, 'L', (40, 15), 0)

# Add edges to graph
graph.add_edge('A', 'C', 35)
graph.add_edge('A', 'E', 60)
graph.add_edge('C', 'A', 35)
graph.add_edge('C', 'J', 7)
graph.add_edge('E', 'H', 11)
graph.add_edge('E', 'A', 60)
graph.add_edge('H', 'E', 11)
graph.add_edge('H', 'L', 20)
graph.add_edge('J', 'C', 7)
graph.add_edge('J', 'K', 12)
graph.add_edge('K', 'J', 12)
graph.add_edge('K', 'L', 5)
graph.add_edge('L', 'K', 5)
graph.add_edge('L', 'H', 20)


# print nodes info.
Ex.print_nodes_info(graph)

# print neighbors for each node.
Ex.print_neighbors(graph)

# execute A* algorithm with Euclidean distance heuristic.
Ex.execute(1, graph)

# execute A* algorithm with Manhattan distance heuristic.
Ex.execute(2, graph)

# execute A* algorithm with Steps heuristic.
Ex.execute(3, graph)
