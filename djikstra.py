##############################################################
#
# Djiskstra algorithm, by using a table of distante.
# The shortest path between node A and node B is the path with the
# minimum summary weight.
# IMPORTANT : For weighted graph
#
##############################################################
from typing import ItemsView
import priority_dict

from graph import *


def build_distance_table(graph, source):

    # A dictionnary mapping from the vertex number to a tuple of
    # (distance_from_source, last vertex seen on path from source)
    distance_table = {}

    # initiate distance table
    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    # The distance from the source itself is 0
    distance_table[source] = (0, source)

    # Holds mapping on vertex id to distance from source
    # Access to the highest priority  (lowest distance) Item first.
    # priorityQueue[vertex] = distance; where the distance value forms that priority.
    priority_queue = priority_dict.priority_dict()

    # The distance from the source of the source is =0
    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:
        # Process the vertex with the smallest priority (=weight)
        current_vertex = priority_queue.pop_smallest()

        # The distance of the current node from the source
        current_distance = distance_table[current_vertex][0]

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # Calculate the new distance
            distance = current_distance + \
                g.get_edge_weight(current_vertex, neighbor)

            # Recorded the last distance of his neighbor from the source
            neighbor_distance = distance_table[neighbor][0]

            # If there is a currently recorded distance from the source and this is
            # greater than the distance of the new path found, update the current
            # distance from the source in the distance table
            if neighbor_distance is None or neighbor_distance > distance:
                distance_table[neighbor] = (distance, current_vertex)
                # We also need to update the priority queue with the distance
                priority_queue[neighbor] = distance

    return distance_table


def shortest_path(graph, source, destination):
    # The shortest_path function is exactly the same as the shortest_path algorithm

    # Build the table_distance
    distance_table = build_distance_table(graph, source)

    # Initialy, in the short path there is only the destination
    # at the end we will backtrack the list to get the shortest_path
    path = [destination]

    # Find the last preceeding node in order to get our distance from the source
    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:
        path = [previous_vertex] + path
        previous_vertex = distance_table[previous_vertex][1]

    if previous_vertex is None:
        print("There is no short path from %d to %d" % (source, destination))
    else:
        path = [source] + path
        print("Shortest path is ", path)


# Test implementation
g = AdjacencyMatrixGraph(8, directed=True)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 5)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(0, 7, 8)


shortest_path(g, 0, 6)
shortest_path(g, 4, 7)
shortest_path(g, 7, 0)
