"""
CtCi
4.9 A binary search tree was created by traversing through an array from left to
right and inserting each element. Given a binary search tree with distinct elements,
print all possible arrays that could have led this tree.

eg.
INPUT:
    2
  1   3
OUTPUT:
 [2, 1, 3], [2, 3, 1]
"""
import copy
from BinarySearchTree import BinarySearchTree

def bst_sequences(node):
    """
    Time: O(n * n!)
    Space: O((nm)!)
    """
    result = []
    if node is None:
        result.append([])
        return result
    prefix = [node.value]
    # get left and right sequences
    left_seqs = bst_sequences(node.left)
    right_seqs = bst_sequences(node.right)

    for left in left_seqs:
        for right in right_seqs:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            for weave in weaved:
                result.append(weave)
    return result

def weave_lists(left, right, weaved, prefix):
    """
    Time: O(n!)
    Space: O((nm)!)
    """
    if len(left) < 1 or len(right) < 1:
        temp = copy.deepcopy(prefix)
        temp.extend(left)
        temp.extend(right)
        weaved.append(temp)
        return
    # both left and right are not empty
    # recurse with head of the first list added to the prefix.
    # remove the head will damage the first, so we'll need to put it back where we found it afterwards
    head = left.pop(0)
    prefix.append(head)
    weave_lists(left, right, weaved, prefix)
    prefix.pop()
    left.insert(0, head)

    # do same thing with second, damaging then restoring the list
    head = right.pop(0)
    prefix.append(head)
    weave_lists(left, right, weaved, prefix)
    prefix.pop()
    right.insert(0, head)

if __name__ == '__main__':
    bst = BinarySearchTree(2)
    bst.insert(1)
    bst.insert(3)
    root = bst.get_root()

    print bst_sequences(root)
    # weaved = []
    # weave_lists([1,2], [3,4], weaved, [])
    # print weaved