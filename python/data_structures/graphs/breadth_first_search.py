"""
Implementation of breadth first search algorithm.

"""
from collections import deque
from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix

def breadth_first_search_1(adj_list, start):
    """
    Implementing BFS with AdjacencyList
    """
    graph = adj_list.get_graph()
    visited = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]

    queue = deque([start])
    dist[start] = 0
    discovered[start] = True
    while len(queue) > 0:
        curr = queue.popleft()
        visited[curr] = True

        # we point the first node in linked list to '.next' because AdjacencyList's head node is the current
        # vertex
        curr_linked_list = graph[curr].get_head().next
        while curr_linked_list is not None:
            if not visited[curr_linked_list.value] and not discovered[curr_linked_list.value]:
                print curr_linked_list.value,
                queue.append(curr_linked_list.value)
                discovered[curr_linked_list.value] = True
                predecessor[curr_linked_list.value] = curr
                dist[curr_linked_list.value] = dist[curr] + 1
            curr_linked_list = curr_linked_list.next
        print ""
    print "visited: ", visited
    print "distance: ", dist
    print "predecessor: ", predecessor
    return



def breadth_first_search_2(adj_matrix, start):
    """
    Implementing BFS with AdjacencyMatrix
    """
    graph = adj_matrix.get_graph()
    visited = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]

    queue = deque([start])
    dist[start] = 0
    discovered[start] = True
    while len(queue) > 0:
        curr = queue.popleft()
        visited[curr] = True

        for i in range(len(graph[curr])):
            if graph[curr][i] == 1 and not visited[i] and not discovered[i]:
                print i,
                queue.append(i)
                discovered[i] = True
                predecessor[i] = curr
                dist[i] = dist[curr] + 1
        print ""
    print "visited: ", visited
    print "distance: ", dist
    print "predecessor: ", predecessor
    return

if __name__ == '__main__':
    adj_list = AdjacencyList(5)
    adj_list.insert_edges(0, [1, 4])
    adj_list.insert_edges(1, [0, 4, 2, 3])
    adj_list.insert_edges(2, [1, 3])
    adj_list.insert_edges(3, [1, 4, 2])
    adj_list.insert_edges(4, [3, 0, 1])
    breadth_first_search_1(adj_list, 0)

    adj_matrix = AdjacencyMatrix(5)
    adj_matrix.insert_edges(0, [1, 4])
    adj_matrix.insert_edges(1, [0, 4, 2, 3])
    adj_matrix.insert_edges(2, [1, 3])
    adj_matrix.insert_edges(3, [1, 4, 2])
    adj_matrix.insert_edges(4, [3, 0, 1])
    breadth_first_search_2(adj_matrix, 0)