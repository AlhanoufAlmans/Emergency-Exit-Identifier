from PriorityQueue import PriorityQueue
import math


def create_dic(graph_, start):
    """
    this method will initialize dictionary with infinite values for all nodes in the map.
    """
    score = dict()
    for node in graph_.nodes:
        score[node[0]] = math.inf
    score[start] = 0
    return score


def heuristic_function(graph_, a, b, option, current_key):
    """
    this method will calculate the heuristic value.
    _____________________________________________________________
   :param current_key: is the key of the current node.
   :param option: is number that will determine which heuristic function will used to find shortest path.
   :param a: is the location of starting node in the Map.
   :param b: is the location of ending node in the Map.
   :param graph_: is a graph contains nodes and edges.
   _____________________________________________________________
   :return: a list contains the shortest path from start to goal.
    """

    # if option is 1 then we use euclidean distance.
    if option == 1:
        return Euclidean_distance(a, b)
        # if option is 2 then we use manhattan distance.
    elif option == 2:
        return Manhattan_distance(a, b)
        # if option is 3 then we use steps heuristic.
    else:
        # current_key we use it to extract steps needs to reach the goal from the current node.
        return Steps(graph_, current_key)


def Steps(graph_, current_key):
    """
    :param graph_: is a graph contains nodes and edges.
    :param current_key: is the key of the current node.
    :return: the steps needs to reach the goal from the current node.
    """
    return graph_.nodes.get(current_key).steps


def goal_test(node, goal):
    """
    this method will check if node equal to goal.
    """
    return node == goal


def Manhattan_distance(a, b):

    (x1, y1) = a  # point a coordinates.
    (x2, y2) = b  # point b coordinates.

    return abs(x1-x2) + abs(y1-y2)


def Euclidean_distance(a, b):
    """
    this method will calculate the distance between two node.
    """
    (x1, y1) = a  # point a coordinates.
    (x2, y2) = b  # point b coordinates.

    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def generate_path(come_from, start, goal, path):
    """
    this method will return the shortest path list after we know the shortest path from start to goal. B: A ,
    """
    # path = []
    # start from the bottom.
    curr = goal
    # add goal to the list.
    path.append(goal)
    while curr != start:
        # insert in the beginning of the list.
        path.insert(0, come_from.get(curr))
        # update current to the next node.
        curr = come_from.get(curr)
    return path


def shortest_path(Graph_, start, goal, option_):
    """
    this method will returns the shortest path between a start point and a goal pint by using A* algorithm.
   _____________________________________________________________
   :param option_: is number that will determine which heuristic function will used to find shortest path.
   :param start:is the number of starting node in the Map.
   :param Graph_: is a graph.
   :param goal: is the number of target node in the Map.
   _____________________________________________________________
   :return: a list contains the shortest path from start to goal.
   """
    # we use this variable to count the number of visited nodes.
    num_expanded = 0
    # if something wrong
    if Graph_ is None or start is None or goal is None:
        return []
    # if starting node equal to goal.
    if goal_test(start, goal):
        return [start]

    # Initialize data structures.
    closed_set = set()  # set for store all explore nodes.
    open_queue = PriorityQueue()  # Queue for store nodes according to its priority which is (f(n)= g(n) +h(n)).
    open_dic = dict()  # this dictionary will track the content of the queue ( for fast look up).
    come_from = {start: None}  # this dictionary will store the parent of each node.
    g_score = create_dic(Graph_, start)  # this dictionary will store the costs of all nodes.
    path = []  # this list will store the shortest path from start to goal.
    Nodes = dict()  # this dictionary contains {key of node : node location(list)}.
    for key, Node in Graph_.nodes.items():
        Nodes.update({key: Node.location})
    Edges = Graph_.Neighbour  # this dictionary contains {key of node : children of that node(list)}.

    # insert the starting node in the open queue and open_dic
    open_queue.push(0, start, 0, 0, Nodes.get(start))
    open_dic.update({start: None})

    num_nodes_PQueue = 1

    while open_queue.size() > 0:
        # pop the node that has the smallest f(n) from the queue.
        curr_node = open_queue.pop()

        # if the current node is equal to the goal.
        if goal_test(curr_node[1].key, goal):
            path = generate_path(come_from, start, goal, path)
            break

        # add the current node to the explore set.
        closed_set.add(curr_node[1].key)
        num_expanded = num_expanded + 1
        # after we popped node from the queue(open_queue) we have to remove it from the open_dic.
        open_dic.pop(curr_node[1].key)

        # bring all children of the current node and do all these instructions for each.
        for k in Edges.get(curr_node[1].key):
            # if the child is not in explore set.
            if k not in closed_set:
                # calculate the heuristic value for the child.
                h = heuristic_function(Graph_, Nodes[k], Nodes.get(goal), option_, k)
                # calculate the cost value for the child.
                g = curr_node[1].cost + Graph_.cost.get((curr_node[1].key, k))
                # the total cost.
                f = g + h

                """if the child is in open_dic and the total cost is greater than or equal to the previous cost for 
                this child then skipped this child."""
                if k in open_dic and f >= g_score[k]:
                    continue
                # else insert child (I=key of the node,g=the cost of the node,f =total cost) to open_queue and open_dic.
                open_queue.push(g, k, curr_node[1].steps, f, Nodes.get(k))
                open_dic.update({k: f})
                num_nodes_PQueue = num_nodes_PQueue + 1
                # update cost of this child in g_cost.
                g_score.update({k: f})
                # change the parent of this child.
                come_from[k] = curr_node[1].key

    print("Number of vested nodes: " , num_expanded , " h(n): ", option_)
    print("Number of nodes in the queue: " , num_nodes_PQueue , " h(n): ", option_)
    return path
