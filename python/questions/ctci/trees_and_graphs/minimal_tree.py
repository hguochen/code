"""
CtCi
4.2 Given a sorted(increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""
from BinarySearchTree import BinarySearchTree

def minimal_tree(tree, array):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the array
    """
    if len(array) < 1:
        return
    mid = len(array) / 2
    if tree is None:
        tree = BinarySearchTree(array[mid])
    else:
        tree.insert(array[mid])
    minimal_tree(tree, array[:mid])
    minimal_tree(tree, array[mid+1:])
    return tree


if __name__ == "__main__":
    arr1 = [3, 9, 10, 27, 38, 43, 82]
    bst = BinarySearchTree(None)
    root = bst.get_root()
    bst.preorder(root)
    print
    result = minimal_tree(None, arr1)
    root = result.get_root()
    result.levelorder(root)
    print
    result.preorder(root)
    print
    result.inorder(root)