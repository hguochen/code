"""
Implementation of red black tree.
Red black tree is a balanced binary search tree.
"""
class Node(object):
    def __init__(self, value, color='R', parent=None, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree(object):
    """docstring for RedBlackTree"""
    def __init__(self, value):
        self.nil = Node(None, 'B') # register a NIL node which all leaf node points to. NIL node is black.
        self.root = Node(value, 'B', self.nil, self.nil, self.nil)

    def insert(self, value):
        node = self.__create_node(value, 'R')
        parent = self.nil
        curr = self.root
        while curr is not self.nil:
            parent = curr
            if node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        node.parent = parent
        if parent is self.nil:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        self.__insert_fix(node)
        return

    def __insert_fix(self, node):
        """
        fix the inserted node so the result tree from root is a red black tree again.
        """
        while node.parent.color == 'R':
            # node's parent is a left child of its grandparent
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                grandparent = node.parent.parent
                if uncle.color == 'R':
                    # case 1: uncle node is RED
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    grandparent.color = 'R'
                else: # uncle.color == 'B'
                    if node == node.parent.right:
                        # case 2: uncle node is BLACK and node is a right child
                        node = node.parent
                        self.__left_rotate(node)
                    # case 3: uncle node is BLACK and node is a left child
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.__right_rotate(node.parent.parent)
            else: # node.parent == node.parent.parent.right
                # node's parent is a right chidl of its grandparent
                uncle = node.parent.parent.left
                grandparent = node.parent.parent
                if uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    grandparent.color = 'R'
                else: # uncle.color == 'B'
                    if node == node.parent.left:
                        # case 2: uncle node is BLACK and node is a left child
                        node = node.parent
                        self.__right_rotate(node)
                    # case 3: uncle node is BLACK and node is a right child
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.__left_rotate(node.parent.parent)
        self.root.color = 'B'
        return

    def __create_node(self, value, color):
        return Node(value, color, self.nil, self.nil, self.nil)

    def search(self, value):
        if self.root == self.nil:
            return
        return self.__search_node(self.root, value)

    def __search_node(self, node, value):
        if node is self.nil:
            return
        if value == node.value:
            return node
        elif value < node.value:
            return self.__search_node(node.left, value)
        else:
            return self.__search_node(node.right, value)

    def delete(self, value):
        # TODO
        pass

    def __left_rotate(self, node):
        # set new_parent
        new_parent = node.right
        # turn new_parent's left sub tree into node's right sub tree
        node.right = new_parent.left

        if new_parent.left is not self.nil:
            new_parent.left.parent = node
        # link node's parent to new_parent's parent
        new_parent.parent = node.parent

        if node.parent is self.nil:
            pass
        elif node == node.parent.left: # node is a left child of its parent
            node.parent.left = new_parent
        else:
            node.parent.right = new_parent
        # put node on new_parent's left
        new_parent.left = node
        node.parent = new_parent
        return

    def __right_rotate(self, node):
        # TODO: draw diagram to figure out right rotate and complete code
        new_parent = node.left
        # turn new parent's right sub tree into node's left sub tree
        node.left = new_parent.right
        # point new parent's right sub tree parent pointer to node if its not none
        if new_parent.right is not self.nil:
            new_parent.right.parent = node
        # new parent's parent point to node's parent
        new_parent.parent = node.parent

        # node's parent now points to new parent
        if node.parent is self.nil:
            self.root = new_parent
        elif node.parent.left == node: # node is a left child
            node.parent.left = new_parent
        else: # node is a right child
            node.parent.right = new_parent
        # move node to become new parent's right child
        new_parent.right = node
        node.parent = new_parent
        return

    def preorder(self, node):
        if node is self.nil:
            return
        print node.value, node.color,
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is self.nil:
            return
        self.inorder(node.left)
        print node.value, node.color,
        self.inorder(node.right)

    def postorder(self, node):
        if node is self.nil:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print node.value, node.color,

    def levelorder(self, node):
        queue = [node]

        while len(queue) > 0:
            curr = queue.pop(0)
            print curr.value, curr.color,
            if curr.left is not self.nil:
                queue.append(curr.left)
            if curr.right is not self.nil:
                queue.append(curr.right)
        print ""
        return

    def get_root(self):
        return self.root

if __name__ == '__main__':
    tree = RedBlackTree(13)
    tree.insert(8)
    tree.insert(17)
    tree.insert(1)
    tree.insert(11)
    tree.insert(15)
    tree.insert(25)
    tree.insert(6)
    tree.insert(22)
    tree.insert(27)
    root = tree.get_root()
    tree.levelorder(root)