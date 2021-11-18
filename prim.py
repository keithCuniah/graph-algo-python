##############################################################
#
# Prim algorithm
# TIs used to find the minimum weight spanning tree
# Note : ONLY for connected graph (=no disjoint)
#
##############################################################
import priority_dict

from graph import *


def spanning_tree(graph, source):
    # A distance mapping from the vertex number to a tuple of
    # (distance from source, last vertex on path from source)
    distance_table = {}

    # Initialize distance_table for all nodes
    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    # The distance of the source from itself =0
    distance_table[source] = (0, source)

    # Hold mapping of the vertex id to distance from source
    # Access the highest priority (lowest distance) item first
    priority_queue = priority_dict.priority_dict()
    priority_queue[source] = 0

    # We maintain a set of visited_vertices to not visite
    # a node twice
    visited_vertices = set()

    # Initiate a spanning tree
    # Set of edges where each edge is a represented by a string
    # '1->2': is an edge between 1 and 2
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:

        # Get the source or the lower priority vortex
        current_vertex = priority_queue.pop_smallest()

        # If we visited the vertex earlier then we have all
        # outbound edges from it, we do not process it again
        if current_vertex in visited_vertices:
            continue

        visited_vertices.add(current_vertex)

        # If the current vertex is the source, we haven't traversed an
        # edge yet, no edge to add our spanning tree
        if current_vertex != source:
            # The current_vertex is connected by the lowest weighted edge
            last_vertex = distance_table[current_vertex][1]

            edge = str(last_vertex) + "-->" + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # The distance to the edge is only the weight of the edge
            # connected the neighbor
            distance = graph.get_edge_weight(current_vertex, neighbor)

            # The last recorded distance to the neighbor
            neighbor_distance = distance_table[neighbor][0]

            # If this neighbor has been seen for the first time or the new edge
            # connecting this neighbor is of a lower weight than the last
            if neighbor_distance is None or neighbor_distance > distance:

                # We need to update the distance_table and priority_queue
                distance_table[neighbor] = (distance, current_vertex)

                priority_queue[neighbor] = distance

    for edge in spanning_tree:
        print(edge)


# Test the implementation
g = AdjacencyMatrixGraph(8, directed=False)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

spanning_tree(g, 3)
