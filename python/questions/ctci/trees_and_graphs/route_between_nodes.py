"""
CtCi
4.1 Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""
from AdjacencyList import AdjacencyList

def route_between_nodes(graph, source, dest):
    """
    BFS of dest node starting from source node.
    Time: O(V + E)
    Space: O(V)
    where V is number of vertices, E is number of edges
    """
    if not graph:
        return None
    visited = [False for _ in range(len(graph))]
    queue = [source]

    while len(queue) > 0:
        node_index = queue.pop(0)
        if node_index == dest:
            return True
        visited[node_index] = True
        curr = graph[node_index].get_head()
        while curr is not None:
            if not visited[curr.value] and curr.value not in queue:
                queue.append(curr.value)
            curr = curr.next
    return False

def route_between_nodes_dfs(graph, source, dest):
    """
    DFS of dest node starting from source node.
    Time: O(V + E)
    Space: O(V)
    where V is number of vertices, E is number of edges    
    """
    if not graph:
        return None
    visited = [False for _ in range(len(graph))]
    stack = [source]

    while len(stack) > 0:
        node_index = stack.pop()
        if node_index == dest:
            return True
        visited[node_index] = True
        curr = graph[node_index].get_head()
        while curr is not None:
            if not visited[curr.value] and curr.value not in stack:
                stack.append(curr.value)
            curr = curr.next
    return False

def route_between_nodes_dfs_2(graph, source, dest):
    visited = [False for _ in range(len(graph))]
    return route_between_nodes_dfs_recurs(graph, visited, source, dest)

def route_between_nodes_dfs_recurs(graph, visited, source, dest):
    if source == dest:
        return True
    visited[source] = True
    curr = graph[source].get_head()
    while curr is not None:
        if not visited[curr.value]:
            return route_between_nodes_dfs_recurs(graph, visited, curr.value, dest)
        curr = curr.next
    return False

if __name__ == '__main__':
    graph = AdjacencyList(5)
    graph.insert_edges(0, [1])
    graph.insert_edges(1, [2])
    graph.insert_edges(2, [3])
    graph.insert_edges(3, [])
    graph.insert_edges(4, [])
    graph.print_graph()

    print route_between_nodes(graph.get_graph(), 0, 1)
    print route_between_nodes(graph.get_graph(), 0, 2)
    print route_between_nodes(graph.get_graph(), 0, 3)
    print route_between_nodes(graph.get_graph(), 0, 4)

    print route_between_nodes_dfs(graph.get_graph(), 0, 1)
    print route_between_nodes_dfs(graph.get_graph(), 0, 2)
    print route_between_nodes_dfs(graph.get_graph(), 0, 3)
    print route_between_nodes_dfs(graph.get_graph(), 0, 4)

    print route_between_nodes_dfs_2(graph.get_graph(), 0, 1)
    print route_between_nodes_dfs_2(graph.get_graph(), 0, 2)
    print route_between_nodes_dfs_2(graph.get_graph(), 0, 3)
    print route_between_nodes_dfs_2(graph.get_graph(), 0, 4)
