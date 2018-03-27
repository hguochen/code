"""
Implementation of graph using adjacency list
"""

"""
Singly linked list implementation.

"""

class Node(object):
    """docstring for Node"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self, value):
        self.head = Node(value)

    def insert_front(self, value):
        """
        Insert node at front of the list

        """
        node = Node(value)
        node.next = self.head
        self.head = node
        return

    def insert_back(self, value):
        """
        Insert node at back of the list

        """
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        node = Node(value)
        curr.next = node
        return

    def delete(self, value):
        """
        Delete the node which contains the value
        """
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    self.head = self.head.next
                    return
                prev.next = curr.next
                del curr
                break
            prev = curr
            curr = curr.next
        return

    def get_head(self):
        return self.head
        
    def print_list(self):
        curr = self.head
        while curr is not None:
            print curr.value,
            curr = curr.next
        print ""
        return

    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return False

class AdjacencyList(object):
    def __init__(self, vertice_count):
        self.graph = [LinkedList(i) for i in range(vertice_count)]

    def insert_edges(self, vertice_index, connected_vertices):
        if (vertice_index >= len(self.graph) or
            len(connected_vertices) < 1):
            return
        for vertice in connected_vertices:
            self.graph[vertice_index].insert_back(vertice)
        return

    def get_graph(self):
        return self.graph

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
