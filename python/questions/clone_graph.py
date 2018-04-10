# imagine given a network of nodes, nodes object contains list of nodes to which it is connected
# goal: write a copy function that duplicates the entire structure of the graph
# can have cycles
# directed edge
# no min max size of graph
# connected graph
class Node(object):
    def __init__(self):
        self.nodes = [Node1, Node2, ...] # array of Node object
    
    def insert_node(node):
        self.nodes.append(node)
        return

    def get_nodes():
        return self.nodes

    def get_memory_address():
        pass
# hash table
# key: value? 
# new_node: old_node
# assumption:
# graph could be cyclic or acyclic 
# graph has list of nodes
# graph no min max size
def duplicate_graph(node):
    """
    Time: O(|V| + |E|}
    Space: O(|V| + |E|}
    """
    if node is None:
        return None
    # memory_add_of_old_node: new_cloned_node
    mapping_table = {}
    queue = [node]
    # populating all ndoes into mapping_table
    while len(queue) > 0:
        curr = queue.pop(0)
        # put cloned node into map
        new_curr = Node()
        mapping_table[curr.get_memory_address()] = new_curr
        neighbours = curr.get_nodes()
        for i in xrange(len(neigbhours)):
            address = neighbours[i].get_memory_address()
            if address not in mapping_table:
                new_node = Node()
                mapping_table[address] = new_node
            else:
                new_node = mapping_table[address]
            new_curr.insert_node(new_node)
            # put new neighbours into curr new node
            if neigbhours[i].get_memory_address() not in mapping_table:
                queue.append(neighbours[i]) # visit all nodes
        
    return mapping_table[node.get_memory_address()]

