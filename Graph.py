from PriorityQueue import Node


class Graph:

    def __init__(self):
        self.nodes = dict() # key : Node
        self.Neighbour = dict() # key :
        self.cost = dict() # (A,B) : 10

    def add_node(self, cost, key, location, steps):
        self.nodes.update({key: Node(cost, key, location, steps)})
 # key : location
    def add_edge(self, a, b, cost):
        if self.Neighbour.get(a) == None:
            self.Neighbour.update({a : [b]})
        else:
            self.Neighbour.get(a).append(b)

        self.cost.update({(a, b): cost}) # A --- B
