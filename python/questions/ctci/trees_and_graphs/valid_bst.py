"""
CtCi
4.5 Implement a function to check if a binary tree is a binary search tree

BST property:
let x be a node in a BST. 
the left subtree of x has values less than x value.
the right subtree of x has values equals or more than x value.

Note: In recursive cases, always make sure your base cases and null cases are handled.

"""
import sys

from BinarySearchTree import BinarySearchTree

def valid_bst(root):
    """
    Time: O(n)
    Space: O(logn) on a balanced tree
    There are up to O(lgn) recursive calls on the stack since we may recurse up to the depth of the tree.
    """
    if not root:
        return False
    return valid_bst_recur(root, [float("-inf"), float("inf")])

def valid_bst_recur(node, min_max):
    if node is None:
        return True
    if node.value < min_max[0] or node.value > min_max[1]:
        return False
    if not valid_bst_recur(node.left, [min_max[0], node.value]) or not valid_bst_recur(node.right, [node.value, min_max[1]]):
        return False
    return True        
    # result = valid_bst_recur(node.left, [min_max[0], node.value])
    # if not result:
    #     return result
    # return valid_bst_recur(node.right, [node.value, min_max[1]])

if __name__ == '__main__':
    bst = BinarySearchTree(27)
    bst.insert(9)
    bst.insert(43)
    bst.insert(3)
    bst.insert(10)
    bst.insert(38)
    bst.insert(82)
    root = bst.get_root()
    print valid_bst(root) # True