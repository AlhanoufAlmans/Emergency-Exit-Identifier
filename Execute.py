import A_star
from time import perf_counter_ns
import time


# execute A* algorithm with different heuristics.
def execute(choice, graph):

    # record start time in milliseconds.
    start_time_ms = perf_counter_ns()

    # record start time in seconds.
    start_time_s = time.perf_counter()

    # store the shortest path in result variable.
    result = A_star.shortest_path(graph, 'A', 'L', choice)

    # record end time in milliseconds.
    end_time_s = time.perf_counter()

    # record end time in seconds.
    end_time_ms = perf_counter_ns()

    # print performance in milliseconds.
    print('Performance_in_ms:', end_time_ms - start_time_ms)

    # print performance in seconds.
    print('Performance_in_s:', end_time_s - start_time_s)

    # print shortest path and which heuristic we used to reach this path.
    print('result_for_heuristic_', choice, ': ', result)

    # this line for clean output.
    print("\n ----------------------------------------------------------------\n")


# print nodes info.
def print_nodes_info(graph):
    for i in graph.nodes.items():
        print('key: ', i[1].key, 'location (x,y): ', i[1].location , 'Steps: ', i[1].steps)
    print('\n\n\n')


# print neighbors for each node.
def print_neighbors(graph):
    for i in graph.Neighbour.items():
        print('key: ', i[0], ' Neighbour: ', i[1])
    print('\n\n\n')
