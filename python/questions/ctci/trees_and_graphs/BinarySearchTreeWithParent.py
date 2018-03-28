"""
Implementing binary search tree with parent pointer
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BinarySearchTreeWithParent(object):
    """docstring for BinarySearchTreeWithParent"""
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        return self.insert_node(self.root, node)
    
    def insert_node(self, parent, node):
        if node.value < parent.value:
            if parent.left is None:
                parent.left = node
                node.parent = parent
            else:
                return self.insert_node(parent.left, node)
        else:
            if parent.right is None:
                parent.right = node
                node.parent = parent
            else:
                return self.insert_node(parent.right, node)
        
    def search(self, value):
        if self.root is None:
            return
        curr = self.root
        while curr is not None:
            if value == curr.value:
                return curr
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return

    def delete(self, value):
        if self.root is None:
            return
        node = self.search(value)
        parent = node.parent
        if node is None:
            return
        if node.left is None and node.right is None:
            # case 1: 0 child node
            if node.parent is None:
                self.root = None
                return
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            node.parent = None
        elif node.left is None or node.right is None:
            # case 2: 1 child node
            if node.left is not None:
                if parent is None:
                    self.root = node.left
                    return
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else: # node.right is not None
                if parent is None:
                    self.root = node.right
                    return
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
            node.parent = None
        else:
            # case 3: 2 child nodes
            trav_parent = node
            trav_curr = node.right
            while trav_curr.left is not None:
                trav_parent = trav_curr
                trav_curr = trav_curr.left
            temp = node.value
            node.value = trav_curr.value
            trav_curr.value = temp
            if trav_parent == node:
                trav_parent.right = trav_curr.right
                trav_curr.parent = None
            else:
                trav_parent.left = trav_curr.right
                trav_curr.parent = None
            

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
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            curr = queue.pop(0)
            print curr.value,
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        print ""
        return

    def get_root(self):
        return self.root


if __name__ == "__main__":
    bst = BinarySearchTreeWithParent(8)
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
    print "------------------"
    # print bst.search(8).value
    # print bst.search(3).value
    # print bst.search(10).value
    # print bst.search(1).value
    # print bst.search(6).value
    # print bst.search(4).value
    # print bst.search(7).value
    # print bst.search(14).value
    # print bst.search(13).value
    bst.delete(13)
    bst.preorder(root)
    print ""
    bst.inorder(root)
    print ""
    bst.postorder(root)
    print ""
