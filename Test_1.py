from Graph import Graph
import math
import Execute as Ex

# Create graph
graph = Graph()

# Add nodes to graph
graph.add_node(0, 'A', (35, 50), 0)
graph.add_node(math.inf, 'B', (15, 28), 21)
graph.add_node(math.inf, 'C', (25, 48), 6)
graph.add_node(math.inf, 'D', (50, 37), 15)
graph.add_node(math.inf, 'E', (65, 35), 25)
graph.add_node(math.inf, 'F', (15, 39), 23)
graph.add_node(math.inf, 'G', (40, 35), 18)
graph.add_node(math.inf, 'H', (60, 20), 11)
graph.add_node(math.inf, 'J', (30, 35), 11)
graph.add_node(math.inf, 'K', (25, 20), 3)
graph.add_node(math.inf, 'L', (40, 15), 0)

# Add edges to graph
graph.add_edge('A', 'B', 42)
graph.add_edge('A', 'C', 12)
graph.add_edge('A', 'D', 29)
graph.add_edge('A', 'E', 50)
graph.add_edge('B', 'F', 11)
graph.add_edge('B', 'A', 42)
graph.add_edge('C', 'A', 12)
graph.add_edge('C', 'F', 20)
graph.add_edge('C', 'G', 20)
graph.add_edge('D', 'G', 7)
graph.add_edge('D', 'H', 31)
graph.add_edge('D', 'A', 29)
graph.add_edge('E', 'H', 9)
graph.add_edge('E', 'A', 50)
graph.add_edge('F', 'C', 20)
graph.add_edge('F', 'J', 22)
graph.add_edge('F', 'B', 11)
graph.add_edge('G', 'C', 20)
graph.add_edge('G', 'D', 7)
graph.add_edge('G', 'J', 10)
graph.add_edge('G', 'K', 30)
graph.add_edge('H', 'D', 31)
graph.add_edge('H', 'E', 9)
graph.add_edge('H', 'L', 16)
graph.add_edge('J', 'F', 22)
graph.add_edge('J', 'G', 10)
graph.add_edge('J', 'K', 17)
graph.add_edge('K', 'J', 17)
graph.add_edge('K', 'G', 30)
graph.add_edge('K', 'L', 5)
graph.add_edge('L', 'K', 5)
graph.add_edge('L', 'H', 16)


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
