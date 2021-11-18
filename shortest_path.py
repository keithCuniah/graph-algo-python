##############################################################
#
# Algorithme for calculate shortest path algorithme, by using
# a table of distante.
# The shortest between node A and node B is the path with the
# less hop between A and B.
# IMPORTANT : shortest path is for unweighted graph
#
##############################################################
from queue import Queue
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

    queue = Queue()
    # Initialy, the only distance we know it's the source node from itself =0
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        # The distance of the current_vertex from the source
        current_distance = distance_table[current_vertex][0]

        # check if current_vertex neighbors have been visited
        for neighbor in graph.get_adjacent_vertices(current_vertex):
            # Only update the distance table if no current distant from
            # the source is set
            if distance_table[neighbor][0] is None:
                distance_table[neighbor] = (
                    1 + current_distance, current_vertex)

                # Enqueue the neighbor only if it has other adjacent vertices
                # to explore
                if(len(graph.get_adjacent_vertices(neighbor)) > 0):
                    queue.put(neighbor)

    return distance_table


def shortest_path(graph, source, destination):
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
g = AdjacencySetGraph(8, directed=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(5, 4)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(0, 7)


shortest_path(g, 0, 5)
shortest_path(g, 0, 6)
shortest_path(g, 7, 4)
