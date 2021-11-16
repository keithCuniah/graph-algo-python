import abc

import numpy as np

###################################################################
#
# The base class representation of a graph with all the interface
# methods
# Note : vertex = node
###################################################################


class Graph(abc.ABC):
    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractclassmethod
    def add_edge(self, v1, v2, weight):
        # when not implemented yet, can put "pass" keyword in the method
        pass

    @abc.abstractclassmethod
    def get_adjacent_vertices(self, v):
        # retrieve all adjacent vertices for specified vertex
        pass

    @abc.abstractclassmethod
    def get_indegree(self, v):
        # retrieve the number of degree that are incident on a vertex
        pass

    @abc.abstractclassmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractclassmethod
    def display(self):
        # to use as a debugger
        pass

######################################################################
#
# Represents a graph as an adjacent matrix. A cell in the matrix has
# a value when there exists an edge between the vertex represented by
# the row and a column numbers
# Weighted graphs can hold values > 1 in the matrix cells
# A value of 0 in the cell indicates that there is no edge
#
######################################################################


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        # check that vertices we passed are valid (not outside the bounds of the graph)
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        # sanity check on weight (it"s possible but not using it here)
        if weight < 1:
            raise ValueError("An edge cannot have a weight < 1")

        self.matrix[v1][v2] = weight

        # in case of undirected graph, the adjency matrix is symetrical
        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        # check if v is a valid vertex
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        # adjacent_vertice will be populated
        adjacent_vertices = []
        for i in range(self.numVertices):
            # if any cell have a value > 0
            #   then the vertex i is adjacent to v
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        # check if v is a valid vertex
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


# test adjency matrix graph with 4 vertex
numNodes = 4
g = AdjacencyMatrixGraph(numNodes)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)

for i in range(numNodes):
    print("Adjacent to : ", i, g.get_adjacent_vertices(i))

for i in range(numNodes):
    print("Indegree to : ", i, g.get_indegree(i))

for i in range(numNodes):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight ", i, " ", j, " weight: ", g.get_edge_weight(i, j))

g.display()
