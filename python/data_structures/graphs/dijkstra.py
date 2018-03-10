"""
Implementation of dijkstra algorithm.
CLRS pg 658
"""
import sys
from linked_lists.linked_list import LinkedList

def dijkstra(graph, start):
    """
    Time: O(V^2) where V is number of vertices, E is number of edges
    with a min priority queue implementation, Time: O(VlgV + E)
    """
    visited, dist, parent = {}, {}, {}
    for key in graph.keys():
        visited[key] = False
        dist[key] = sys.maxint
        parent[key] = None
    dist[start] = 0
    index = start

    while False in visited.values():
        visited[index] = True
        edges = graph[index]
        for edge in edges:
            if edge[1] + dist[index] < dist[edge[0]]:
                dist[edge[0]] = edge[1] + dist[index]
                parent[edge[0]] = index
        # get the next smallest distance in which its node is not visited
        # NOTE: this part can be optimized with a min priority queue
        smallest_dist = sys.maxint
        for key, value in dist.iteritems():
            if not visited[key] and value < smallest_dist:
                smallest_dist = value
                index = key
    return (dist, parent)

def path(table, start, end):
    """
    Based on result of running dijkstra algorithm, stored in table, get the path from start to end.
    """
    path_len = 0
    dist, parent = table
    result = {'path': [], 'path_length': path_len}
    if start == end:
        result['path'].append(start)
        return result
    result['path_length'] += dist[end]
    while start != end:
        result['path'].insert(0, end)
        end = parent[end]
    result['path'].insert(0, start)
    return result

if __name__ == '__main__':
    graph = {}
    graph['s'] = [('t', 10), ('y', 5)]
    graph['t'] = [('x', 1), ('y', 2)]
    graph['x'] = [('z', 4)]
    graph['y'] = [('t', 3), ('x', 9), ('z', 2)]
    graph['z'] = [('x', 6), ('s', 7)]
    result = dijkstra(graph, 's')
    print path(result, 's', 't')
