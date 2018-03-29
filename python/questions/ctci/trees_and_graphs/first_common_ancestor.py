"""
CtCi
4.8 Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure. Note:
This is not necessarily a binary search tree.

"""
from BinarySearchTreeWithParent import BinarySearchTreeWithParent

def first_common_ancestor(node1, node2):
    """
    Assume there is a parent pointer for each node.

    Time: O(lgn)
    Space: O(1)
    where n is the size of the binary tree
    """
    if not node1 or not node2:
        return None
    count1 = get_length_to_root(node1)
    count2 = get_length_to_root(node2)
    curr1, curr2 = node1, node2
    while count1 > count2:
        count1 -= 1
        curr1 = curr1.parent
    while count2 > count1:
        count2 -= 1
        curr2 = curr2.parent
    # now curr1 and curr2 are same length towards root node
    while curr1 is not None:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.parent
        curr2 = curr2.parent
    return None

def get_length_to_root(node):
    count = 0
    while node is not None:
        count += 1
        node = node.parent
    return count

def first_common_ancestor_2(root, node1, node2):
    """
    Assume there is no parent pointer for each node.
    We traverse down starting from the root node.
    If n1 and n2 are on same side, we traverse down that side
    on the first occurence of n1 on 1 side and n2 on the other. we return that node.

    Time: O(lgn)
    Space: O(lgn)
    where n is the size of the binary tree at root.
    """
    if not root or not node1 or not node2:
        return None
    elif not covers(root, node1) or not covers(root, node2):
        return None
    curr = root
    while curr is not None:
        n1_left = covers(curr.left, node1)
        n2_left = covers(curr.left, node2)
        if n1_left != n2_left:
            return curr
        if n1_left:
            curr = curr.left
        else:
            curr = curr.right

def covers(root, node):
    if not root or not node:
        return False
    if root is node:
        return True
    return covers(root.left, node) or covers(root.right, node)


if __name__ == '__main__':
    bst = BinarySearchTreeWithParent(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    root = bst.get_root()
    node1 = bst.search(1)
    node2 = bst.search(2)
    node3 = bst.search(3)
    node5 = bst.search(5)
    node6 = bst.search(6)
    print first_common_ancestor(node1, node3).value
    print first_common_ancestor(node1, node5).value
    print first_common_ancestor(node1, node6).value
    print first_common_ancestor(node1, node2).value

    print first_common_ancestor_2(root, node1, node3).value
    print first_common_ancestor_2(root, node1, node5).value
    print first_common_ancestor_2(root, node1, node6).value
    print first_common_ancestor_2(root, node1, node2).value