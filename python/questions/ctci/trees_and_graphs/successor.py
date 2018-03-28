"""
CtCi
4.6 Write an algorithm to find the "next" node (ie. in-order successor) of a given
node in a binary search tree. You may assume that each node has a link to its parent.
"""
from BinarySearchTreeWithParent import BinarySearchTreeWithParent

def successor(node):
    """
    Given a bst and a node, find the next node in its in order traversal. 
    Time: O(lgn)
    Space: O(1)
    """
    if not node:
        return None
    if node.right is None:
        #case 1: node.right is None, find the first left ancestor
        curr = node.parent
        while curr is not None and curr.right == node:
            node = curr
            curr = curr.parent
        return curr
    else: # node.right is not None
        # case 2: node.right is not None, find the smallest value rooted at node.right
        curr = node.right
        # find the least value rooted at input node
        while curr.left is not None:
            curr = curr.left
        return curr

if __name__ == '__main__':
    bst = BinarySearchTreeWithParent(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.insert(15)
    bst.insert(25)
    bst.insert(35)
    bst.insert(45)
    bst.insert(55)
    bst.insert(65)
    bst.insert(75)
    bst.insert(85)
    root = bst.get_root()
    bst.levelorder(root)
    value_30 = bst.search(30)
    value_70 = bst.search(70)
    value_50 = bst.search(50)
    value_25 = bst.search(25)
    value_35 = bst.search(35)
    value_85 = bst.search(85)
    print successor(value_30).value # 35
    print successor(value_70).value # 75
    print successor(value_50).value # 55
    print successor(value_25).value # 30
    print successor(value_35).value # 40
    print successor(value_85) # None
