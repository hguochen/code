"""
CtCi
4.12 You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that
sum to a given value. The path does not need to start or end at the root or a leaf,
but it must go downwards(travelling only from parent ndoes to child nodes).

BCR: 
Time: O(n)
Space: O(n)
"""

import copy

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)
        self.count = 1

    def get_root(self):
        return self.root

    def insert(self, value, parent, direction):
        if parent is None:
            return
        node = Node(value)
        if direction == "L":
            parent.left = node
        elif direction == "R":
            parent.right = node
        self.count += 1
        return node

    def find(self, value):
        return find_node(self.root, value)

    def find_node(self, node, value):
        if node is None:
            return
        if node.value == value:
            return node
        find_node(node.left, value)
        find_node(node.right, value)

    def delete(self, value):
        if self.root is None:
            return
        parent, node = find_node_and_parent(self.root, None, value)
        if node is None:
            return
        if node.left is None or node.right is None:
            # case 1: node has 0 child
            # case 2: node has 1 child
            if node.left is None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
        else:
            # case 3: node has 2 children
            # get the right most children to replace this node
            parent_curr = node
            curr = node.right
            while curr.right is not None:
                parent_curr = curr
                curr = curr.right
            curr.value, node.value = node.value, curr.value
            parent.right = None
        self.count -= 1
        return

    def find_node_and_parent(self, node, parent, value):
        if node is None:
            return
        if node.value == value:
            return [parent, node]
        parent = node
        find_node_and_parent(node.left, parent, value)
        find_node_and_parent(node.right, parent, value)

    def get_random_node(self):
        if self.count == 0:
            return
        value = random.randint(1, self.count)
        return self.get_random_node_recur(self.root, value)

    def preorder(self, node):
        if node is None:
            return
        print node.value,
        self.preorder(node.left)
        self.preorder(node.right)

    def get_random_node_recur(self, node, count):
        if node is None:
            return
        if count == 1:
            return node
        return get_random_node_recur(node.left, count - 1) or get_random_node_recur(node.right, count - 1)


class Result(object):
    def __init__(self):
        self.count = 0
        self.results = []

def paths_with_sum(node, value, result):
    """
    Time: O(nlgn)
    Space: O(n)
    """
    if node is None:
        return
    get_paths(node, value, result)
    paths_with_sum(node.left, value, result)
    paths_with_sum(node.right, value, result)
    print result.count
    print result.results
    return result

def get_paths(node, value, result):
    if node is None:
        return
    return get_paths_recur(node, value, 0, [], result)

def get_paths_recur(node, value, curr_sum, curr_path, result):
    """
    Time: O(lgn)
    Space: O(n)
    where n is the size of tree rooted at node
    """
    if node is None:
        return
    curr_sum += node.value
    curr_path.append(node.value)
    if curr_sum == value:
        result.count += 1
        result.results.append(copy.deepcopy(curr_path))
    get_paths_recur(node.left, value, curr_sum, curr_path, result)
    get_paths_recur(node.right, value, curr_sum, curr_path, result)
    curr_sum -= node.value
    curr_path.pop()
    return


if __name__ == '__main__':
    bt = BinaryTree(10)
    root = bt.get_root()
    node1 = bt.insert(5, root, "L")
    node2 = bt.insert(-3, root, "R")
    node3 = bt.insert(3, node1, "L")
    node4 = bt.insert(2, node1, "R")
    node5 = bt.insert(11, node2, "R")
    node6 = bt.insert(3, node3, "L")
    node7 = bt.insert(-2, node3, "R")
    node8 = bt.insert(1, node4, "R")
    node9 = bt.insert(-6, node8, "R")
    node10 = bt.insert(6, node9, "R")
    bt.preorder(root)
    paths_with_sum(root, 8, Result())
