"""
CtCi
T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create
an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree
of n is identical of T2. THat is, if you cut off the tree at node n, the two trees
would be identical.
"""
from BinarySearchTree import BinarySearchTree

def check_subtree(root1, root2):
    """
    Return True if tree at root2 is a subtree of tree at root1. False otherwise
    Time: O(mn)
    Space: O(lgn + lgm)
    where m is the size of tree with root1, n is size of tree with root2
    """
    candidates = []
    get_nodes_with_value(root1, root2.value, candidates)
    if not candidates:
        return False
    for node in candidates:
        if is_same_tree(node, root2):
            return True
    return False

def get_nodes_with_value(node, value, candidates):
    if node is None:
        return
    if node.value == value:
        candidates.append(node)
    get_nodes_with_value(node.left, value, candidates)
    get_nodes_with_value(node.right, value, candidates)
    return

def is_same_tree(root1, root2):
    """
    Return True if both trees are the same, else return false
    Time: O(n)
    Space: O(n)
    where n is the size of tree with root2
    """
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.value != root2.value:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)

def check_subtree_2(root1, root2):
    """
    Time: O(n+m)
    Space: O(n+m)
    """
    order1, order2 = [], []
    preorder(root1, order1)
    preorder(root2, order2)
    str1 = "".join(str(e) for e in order1)
    str2 = "".join(str(e) for e in order2)
    return str2 in str1

def preorder(node, order):
    if node is None:
        order.append("X")
        return
    order.append(node.value)
    preorder(node.left, order)
    preorder(node.right, order)

if __name__ == '__main__':
    bst1 = BinarySearchTree(50)
    bst1.insert(20)
    bst1.insert(60)
    bst1.insert(10)
    bst1.insert(25)
    bst1.insert(70)
    bst1.insert(5)
    bst1.insert(15)
    bst1.insert(65)
    bst1.insert(80)
    root1 = bst1.get_root()

    bst2 = BinarySearchTree(60)
    bst2.insert(70)
    bst2.insert(65)
    bst2.insert(80)
    root2 = bst2.get_root()

    print check_subtree(root1, root2)
    print check_subtree_2(root1, root2)