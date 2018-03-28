"""
CtCi
4.4 Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the heights of
the two subtrees of any node never differ by more than one.
"""
import sys
from BinarySearchTree import BinarySearchTree

def check_balanced(root):
    """
    Return True if tree is balanced, else return False.
    Time: O(n)
    Space: O(1)
    """
    if not root:
        return False
    min_max = [sys.maxint, 1]
    check_balanced_recur(root, 1, min_max)
    return min_max[1] - min_max[0] <= 1

def check_balanced_recur(node, count, min_max):
    # pre order traversal
    if node is None:
        return
    if node.left is None and node.right is None:
        if count < min_max[0]:
            min_max[0] = count
        if count > min_max[1]:
            min_max[1] = count
    check_balanced_recur(node.left, count + 1, min_max)
    check_balanced_recur(node.right, count + 1, min_max)

if __name__ == '__main__':
    bst1 = BinarySearchTree(27)
    bst1.insert(9)
    bst1.insert(3)
    bst1.insert(1)
    bst1.insert(53)
    root1 = bst1.get_root()
    print check_balanced(root1) # false

    bst2 = BinarySearchTree(27)
    bst2.insert(9)
    bst2.insert(3)
    bst2.insert(1)
    bst2.insert(53)
    bst2.insert(30)
    root2 = bst2.get_root()
    print check_balanced(root2) # True