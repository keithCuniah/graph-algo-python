######################################################
#
# Breadth-first and  Depth first traversal algorithms
#
######################################################
from queue import Queue
from graph import *


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)
    # note : we use queue because it's a FIFO (First In First Out)
    # => the node we add first to the queue will be dequeued first

    # we keep a visited array to keep the track of the vertices wich have been visited
    # => to not visit a vertex more than once
    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        # retrieve the first node of the queue
        vertex = queue.get()

        # If the vertex have already been visited
        # => we continue to the next node
        if visited[vertex] == 1:
            continue

        # At this point, we have visited a vertex
        print('Visited: ', vertex)
        # so the vertex is marked as 'visited'
        visited[vertex] = 1

        # wre need to access all the neighboors of this vertex
        for v in graph.get_adjacent_vertices(vertex):
            # If these neighboors vertices haven't been  visited yet
            # => we add them to the very END of the queue
            if visited[v] != -1:
                queue.put(v)


def depth_first(graph, visited, current=0):
    # if current node have already been visited we end the recursion
    if visited[current] == 1:
        return

    # we mark the current node as visited
    visited[current] = 1

    print('Visit: ', current)

    # Iterates over all neighboors of current vertex
    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


# testing implementations
g = AdjacencyMatrixGraph(9, directed=False)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

# breadth_first algorithm
# breadth_first(g, 0)

# depth_first algorithm
visited = np.zeros(g.numVertices)
depth_first(g, visited)
