"""
Implementation of topological sort.
CLRS pg 613.
"""
from linked_lists.linked_list import LinkedList

def topological_sort(graph):
    """
    Time: O(V + E) where v is number of vertices, E is number of edges
    Space: O(V)
    """
    visited = {}
    discovered = {}
    for key in graph.keys():
        visited[key] = False
        discovered[key] = False
    result = []
    for key, l_list in graph.iteritems():
        if not visited[key]:
            dfs_visit(graph, key, visited, discovered, result)
    return result

def dfs_visit(graph, start, visited, discovered, result):
    discovered[start] = True
    if graph[start] is not None:
        curr = graph[start].get_head()
        while curr is not None:
            if not visited[curr.value] and not discovered[curr.value]:
                dfs_visit(graph, curr.value, visited, discovered, result)
            curr = curr.next
    visited[start] = True
    result.insert(0, start)


if __name__ == '__main__':
    graph = {}
    graph['undershorts'] = LinkedList('shoes')
    graph['undershorts'].insert_back('pants')
    graph['socks'] = LinkedList('shoes')
    graph['watch'] = None
    graph['pants'] = LinkedList('shoes')
    graph['pants'].insert_back('belt')
    graph['shoes'] = None
    graph['belt'] = LinkedList('jacket')
    graph['shirt'] = LinkedList('belt')
    graph['shirt'].insert_back('tie')
    graph['tie'] = LinkedList('jacket')
    graph['jacket'] = None

    graph['undershorts'].print_list()
    graph['socks'].print_list()
    # print graph['watch'].print_list()
    graph['pants'].print_list()
    # print graph['shoes'].print_list()
    graph['belt'].print_list()
    graph['shirt'].print_list()
    graph['tie'].print_list()
    # print graph['jacket'].print_list()
    
    print topological_sort(graph)