"""
Implementation of graph using adjacency matrix
"""

class AdjacencyMatrix(object):
    """docstring for AdjacencyMatrix"""
    def __init__(self, vertice_count):
        self.graph = [[0 for _ in range(vertice_count)] for _ in range(vertice_count)]

    def insert_edges(self, vertice_index, connected_vertices):
        if (vertice_index >= len(self.graph) or
            len(connected_vertices) < 1):
            return
        for vertice in connected_vertices:
            self.graph[vertice_index][vertice] = 1

    def get_graph(self):
        return self.graph

    def print_graph(self):
        for row in self.graph:
            print row
        print ""


if __name__ == '__main__':
    graph = AdjacencyMatrix(5)
    graph.print_graph()
    graph.insert_edges(0, [1, 4])
    graph.insert_edges(1, [0, 4, 2, 3])
    graph.insert_edges(2, [1, 3])
    graph.insert_edges(3, [1, 4, 2])
    graph.insert_edges(4, [3, 0, 1])
    graph.print_graph()