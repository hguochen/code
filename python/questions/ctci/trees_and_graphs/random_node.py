"""
CtCi
4.11 You are implementing a binary tree class from scratch which, in addition to insert,
find, and delete, has a method getRandomNode() which returns a random node from the
tree. All ndoes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
"""

import random

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)
        self.count = 1

    def insert(self, value, parent, direction):
        if parent is None:
            return
        node = Node(value)
        if direction == "L":
            parent.left = node
        elif direction == "R":
            parent.right = node
        self.count += 1
        return

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

    def get_random_node_recur(self, node, count):
        if node is None:
            return
        if count == 1:
            return node
        return get_random_node_recur(node.left, count - 1) or get_random_node_recur(node.right, count - 1)

if __name__ == '__main__':
    pass