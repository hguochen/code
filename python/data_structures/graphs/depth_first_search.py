"""
Implementation of depth first search algorithm
"""

from AdjacencyList import AdjacencyList
from AdjacencyMatrix import AdjacencyMatrix

def depth_first_search_recursive_1(adj_list):
    graph = adj_list.get_graph()
    visited = [False for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]

    for i in xrange(len(graph)):
        if not visited[i]:
            path_len = 0
            dfs_visit(graph, i, visited, discovered, dist, predecessor, path_len)
        print ""

def dfs_visit(graph, start, visited, discovered, dist, predecessor, path_len):
    print start,
    discovered[start] = True
    connected_vertex = graph[start].get_head().next
    while connected_vertex is not None:
        if not visited[connected_vertex.value] and not discovered[connected_vertex.value]:
            predecessor[connected_vertex.value] = start
            dfs_visit(graph, connected_vertex.value, visited, discovered, dist, predecessor, path_len+1)
        connected_vertex = connected_vertex.next
    visited[start] = True
    dist[start] = path_len
    return

def depth_first_search_iterative_1(adj_list):
    graph = adj_list.get_graph()
    visited = [False for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]
    stack = []

    for i in xrange(len(graph)):
        if not visited[i]:
            path_len = 0
            discovered[i] = True
            dist[i] = path_len
            stack.append(i)

            while len(stack) > 0:
                index = stack.pop()
                print index,
                visited[index] = True
                connected_vertex = graph[index].get_head().next
                while connected_vertex is not None:
                    if not visited[connected_vertex.value] and not discovered[connected_vertex.value]:
                        dist[i] = path_len + 1
                        predecessor[connected_vertex.value] = index
                        discovered[connected_vertex.value] = True
                        stack.append(connected_vertex.value)
                    connected_vertex = connected_vertex.next
            print ""

def depth_first_search_recursive_2(adj_matrix):
    graph = adj_matrix.get_graph()
    visited = [False for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]

    for i in xrange(len(graph)):
        if not visited[i]:
            path_len = 0
            dfs_visit_2(graph, i, visited, discovered, dist, predecessor, path_len)
        print ""

def dfs_visit_2(graph, start, visited, discovered, dist, predecessor, path_len):
    print start,
    discovered[start] = True
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i] and not discovered[i]:
            predecessor[i] = start
            dfs_visit_2(graph, i, visited, discovered, dist, predecessor, path_len+1)
    visited[start] = True
    dist[start] = path_len
    return

def depth_first_search_iterative_2(adj_matrix):
    graph = adj_matrix.get_graph()
    visited = [False for _ in range(len(graph))]
    discovered = [False for _ in range(len(graph))]
    dist = [None for _ in range(len(graph))]
    predecessor = [None for _ in range(len(graph))]
    stack = []

    for i in xrange(len(graph)):
        if not visited[i]:
            path_len = 0
            discovered[i] = True
            dist[i] = path_len
            stack.append(i)
            while len(stack) > 0:
                index = stack.pop()
                print index,
                visited[index] = True
                for j in range(len(graph[index])):
                    if graph[index][j] == 1 and not visited[j] and not discovered[j]:
                        discovered[j] = True
                        predecessor[j] = index
                        stack.append(j)
            print ""

def DFS(adj_list, start):
    graph = adj_list.get_graph()
    visited = [False for _ in range(len(graph))]
    DFS_util(graph, start, visited)
    return

def DFS_util(graph, start, visited):
    visited[start] = True
    print start,

    connected_vertex = graph[start].get_head().next
    while connected_vertex is not None:
        if not visited[connected_vertex.value]:
            DFS_util(graph, connected_vertex.value, visited)
        connected_vertex = connected_vertex.next

if __name__ == '__main__':
    adj_list = AdjacencyList(5)
    adj_list.insert_edges(0, [1, 4])
    adj_list.insert_edges(1, [0, 4, 2, 3])
    adj_list.insert_edges(2, [1, 3])
    adj_list.insert_edges(3, [1, 4, 2])
    adj_list.insert_edges(4, [3, 0, 1])
    print "DFS recursive with adjacency list data structure"
    depth_first_search_recursive_1(adj_list)
    print "DFS iterative with adjacency list data structure"
    depth_first_search_iterative_1(adj_list)
    print ""
    print "DFS simple recursion version"
    DFS(adj_list, 0)

    adj_matrix = AdjacencyMatrix(5)
    adj_matrix.print_graph()
    adj_matrix.insert_edges(0, [1, 4])
    adj_matrix.insert_edges(1, [0, 4, 2, 3])
    adj_matrix.insert_edges(2, [1, 3])
    adj_matrix.insert_edges(3, [1, 4, 2])
    adj_matrix.insert_edges(4, [3, 0, 1])
    print "DFS recursive with adjacency matrix data structure"
    depth_first_search_recursive_2(adj_matrix)
    depth_first_search_iterative_2(adj_matrix)
