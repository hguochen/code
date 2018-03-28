"""
CtCi
4.7 You are given a list of projects and a list of dependencies(which is a list of pairs of projects,
where the second project is dependent on the first project). All of a project's dependencies must be
built before the project is. Find a build order that will allow the projects to be built. If there is
no valid build order, return an error.

Eg.
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output:
    f, e, a, b, d, c
"""

from AdjacencyList import AdjacencyList

def build_order(graph):
    """
    Topological sort. DFS approach.

    The approach works by assuming there are no cycles in the graph(acyclic).
    If there are possible cycles in graph, we can detect cycles by introducing a
    intermediary list similar to visited list. when the recursion hits a 'visiting'
    node again, we know we have hit a cycle in the graph.

    Note: There are no solutions to topological sort if there's a cycle in the graph.
    Time: O(V+E)
    Space: O(V)
    where V is number of vertices, E is number of edges
    """
    if not graph:
        return []
    visited = [False for _ in range(len(graph))]
    result = []
    for i in range(len(graph)):
        build_order_recur(graph, i, visited, result)
    return result

def build_order_recur(graph, idx, visited, result):
    if visited[idx]:
        return
    visited[idx] = True
    curr = graph[idx].get_head()
    while curr is not None:
        if not visited[curr.value]:
            build_order_recur(graph, curr.value, visited, result)
        curr = curr.next
    result.insert(0, idx)
    return

if __name__ == '__main__':
    # 0 -> a
    # 1 -> b
    # 2 -> c
    # 3 -> d
    # 4 -> e
    # 5 -> f
    legend = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
    }
    adj_list = AdjacencyList(6)
    adj_list.insert_edges(0, [3])
    adj_list.insert_edges(1, [3])
    adj_list.insert_edges(2, [])
    adj_list.insert_edges(3, [2])
    adj_list.insert_edges(4, [])
    adj_list.insert_edges(5, [0, 1])
    graph = adj_list.get_graph()

    result = build_order(graph)
    for value in result:
        print legend[value],
    print