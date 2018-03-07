"""
Implementation of binary search tree
"""
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, value):
        super(BinarySearchTree, self).__init__()
        self.root = Node(value)

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        self.insert_node(self.root, node)
        return

    def insert_node(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self.insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert_node(root.right, node)
        return


    def delete(self, value):
        parent, node = self.get_parent_child_nodes(None, self.root, value)
        if node.left is None and node.right is None:
            # no child nodes
            if parent is None:
                node = None
                return
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None or node.right is None:
            if parent is None:
                if node.left is not None:
                    self.root = node.left
                else:
                    self.root = node.right
                del node
            elif node.left is not None:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            elif node.right is not None:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            else: # node.right is not None
                pass
        else:
            # 2 child nodes
            # with node.right as starting point, find node.right's leftmost node.
            # swap the leftmost node value with the given value
            # then delete the leftmost node
            trav_parent = node
            trav_curr = node.right

            while trav_curr.left is not None:
                trav_parent = trav_curr
                trav_curr = trav_curr.left
            # swap leaf node value with the node value to be deleted
            temp = node.value
            node.value = trav_curr.value
            trav_curr.value = temp
            if trav_parent == node:
                trav_parent.right = trav_curr.right
            else:
                trav_parent.left = trav_curr.right
        return

    def get_parent_child_nodes(self, parent, node, value):
        if node is None:
            return None
        if node.value == value:
            return (parent, node)
        elif value < node.value:
            return self.get_parent_child_nodes(node, node.left, value)
        else:
            return self.get_parent_child_nodes(node, node.right, value)


    def search(self, value):
        if self.root is None:
            return
        return self.get_node(self.root, value)
    
    def get_node(self, node, value):
        if node is None:
            return
        if node.value == value:
            return node
        elif value < node.value:
            return self.get_node(node.left, value)
        else:
            return self.get_node(node.right, value)

    def preorder(self, node):
        if node is None:
            return
        print node.value,
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print node.value,
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print node.value,

    def levelorder(self, node):
        queue = [node]

        while len(queue) > 0:
            curr = queue.pop(0)
            print curr.value,
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return

    def get_root(self):
        return self.root

    def min_node(self, node):
        """
        get the minimum node root at node
        """
        if node is None:
            return
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def max_node(self, node):
        """
        get the maximum node rooted at node
        """
        if node is None:
            return
        curr = node
        while curr.right is not None:
            curr = curr.right
        return curr

    def successor(self, value):
        parent, node = self.get_parent_child_nodes(None, self.root, value)
        if node is None:
            return
        # case 1: node has a right node. so we get the left most node in the right child as successor
        if node.right is not None:
            return self.min_node(node.right)
        # a boundary case, node is the root node and since node.right is None, there is no successor anymore.
        if parent is None:
            return
        # case 2: node does not have a right node. we repeatedly traverse up the tree until we find a node
        # where the node is a left child of the parent. then return the parent
        while parent is not None and node == parent.right:
            parent, node = self.get_parent_child_nodes(None, self.root, parent.value)
        return parent

    def predecessor(self, value):
        parent, node = self.get_parent_child_nodes(None, self.root, value)
        if node is None:
            return
        # case 1: node has a left node, so we get the right most node in the left child as predecessor
        if node.left is not None:
            return self.max_node(node.left)
        # boundary case, node is the root node and node.left is None, there is no predecessor anymore.
        if parent is None:
            pass
        while parent is not None and node == parent.left:
            parent, node = self.get_parent_child_nodes(None, self.root, parent.value)
        return parent


if __name__ == '__main__':
    bst = BinarySearchTree(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)
    bst.insert(14)
    bst.insert(13)
    root = bst.get_root()
    bst.preorder(root)
    print ""
    bst.inorder(root)
    print ""
    bst.postorder(root)
    print ""
    bst.levelorder(root)
    print ""
    # print bst.search(8).value
    # print bst.search(3).value
    # print bst.search(10).value
    # print bst.search(1).value
    # print bst.search(6).value
    # print bst.search(14).value
    # print bst.search(4).value
    # print bst.search(7).value
    # print bst.search(13).value    
    # print bst.min_node(root).value
    # print bst.max_node(root).value
    print bst.successor(13).value
    print bst.predecessor(3).value

    bst.delete(6)
    bst.preorder(root)
    print ""
    bst.inorder(root)
    print ""
    bst.postorder(root)
    print ""