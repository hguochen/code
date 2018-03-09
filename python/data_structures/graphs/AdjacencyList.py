"""
Implementation of graph using adjacency list
"""
from linked_lists.linked_list import LinkedList

class AdjacencyList(object):
    """docstring for AdjacencyList"""
    def __init__(self, vertice_count):
        self.graph = [LinkedList(i) for i in range(vertice_count)]

    def insert_edges(self, vertice_index, connected_vertices):
        if (vertice_index >= len(self.graph) or
            len(connected_vertices) < 1):
            return
        for vertice in connected_vertices:
            self.graph[vertice_index].insert_back(vertice)
        return

    def print_graph(self):
        for vertice in self.graph:
            vertice.print_list()


if __name__ == '__main__':
    graph = AdjacencyList(5)
    graph.insert_edges(0, [1, 4])
    graph.insert_edges(1, [0, 4, 2, 3])
    graph.insert_edges(2, [1, 3])
    graph.insert_edges(3, [1, 4, 2])
    graph.insert_edges(4, [3, 0, 1])
    graph.print_graph()