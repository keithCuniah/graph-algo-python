##############################################################
#
# Kruskal algorithm
# IT is used to find the minimum weight spanning tree
# Note : Works for connected graph AND disjoint graph (forest)
#
##############################################################
import priority_dict

from graph import *


def spanning_tree(graph):

    # Instantiate the priority queue
    # Holds a mapping from a pair of edges to the edge weight
    # The edge weight is the priority edge
    priority_queue = priority_dict.priority_dict()

    for v in range(graph.numVertices):
        for neighbor in graph.get_adjacent_vertices(v):

            # Priority_queue is a dict(edge)= weight
            priority_queue[(v, neighbor)] = graph.get_edge_weight(v, neighbor)

    visited_vertices = set()

    # Maps a node to all its adjacent nodes which are in the
    # minimum spanning tree
    spanning_tree = {}

    for v in range(graph.numVertices):
        spanning_tree[v] = set()

    # Number of edge we have got so far
    num_edges = 0

    while len(priority_queue.keys()) > 0 and num_edges < graph.numVertices - 1:

        # Access the lowest cost edge
        v1, v2 = priority_queue.pop_smallest()

        # If we encountered the edge v2 to v1 before
        # => we continue to next
        if v1 in spanning_tree[v2]:
            continue

        # Arrange the spanning tree so the node with the smaller
        # vertex id is always first. This greatly simplifies the
        # code to find cycle in this tree
        vertex_pair = sorted([v1, v2])

        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        # Check if adding the current edge causes a cycle
        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue

        # If edge have been successfully added to the spanning tree
        num_edges = num_edges + 1

        # And mark pboth vertices as visisted
        visited_vertices.add(v1)
        visited_vertices.add(v2)

    print("Visited vertices: ", visited_vertices)

    # If we haven't visited all the vertices in this graph
    # => the spanning tree has not been found
    if len(visited_vertices) != graph.numVertices:
        print("The spanning tree has not been found :(")
    else:
        print("Minimum spanning tree:")
        for key in spanning_tree:
            for value in spanning_tree[key]:
                print(key, "-->", value)


def has_cycle(spanning_tree):

    for source in spanning_tree:
        # Initiate a queue
        q = []
        q.append(source)

        # Keep in track the visited vertices
        visited_vertices = set()

        while len(q) > 0:

            vertex = q.pop(0)

            # If we've see the vertex before in this spanning tree
            # there is a cycle => return True
            # Else we had the vertex to the visited_vertices
            if vertex in visited_vertices:
                return True
            visited_vertices.add(vertex)

            # Add all vertices connected by edges in this spanning tree
            q.extend(spanning_tree[vertex])

    # Return False if we haven't found any cycle
    return False


# Test the implementation
g = AdjacencyMatrixGraph(8, directed=False)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 2)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

spanning_tree(g)
