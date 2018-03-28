"""
CtCi
4.3 Given a binary tree, design an algorithm which creates a linked list
of all the nodes at each depth(eg. if you have a tree with depth D, you'll have
D linked lists.)
"""

from BinarySearchTree import BinarySearchTree
from LinkedList import LinkedList

def list_of_depths(root):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the binary tree.
    """
    if not root:
        return None
    # each element is a linked list, in ascending level
    results = []
    queue = [[0, root]]
    while len(queue) > 0:
        l_list, node = queue.pop(0)
        if len(results) == l_list: # list not contained in result
            results.append(LinkedList(node.value))
        else:
            results[-1].insert_back(node.value)
        if node.left is not None:
            queue.append([l_list+1, node.left])
        if node.right is not None:
            queue.append([l_list+1, node.right])
    return results

if __name__ == "__main__":
    arr1 = [3, 9, 10, 27, 38, 43, 82]
    bst = BinarySearchTree(27)
    bst.insert(9)
    bst.insert(3)
    bst.insert(10)
    bst.insert(43)
    bst.insert(38)
    bst.insert(82)
    root = bst.get_root()
    # bst.levelorder(root)

    results = list_of_depths(root)
    for result in results:
        result.print_list()
