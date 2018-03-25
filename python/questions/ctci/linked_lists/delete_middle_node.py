"""
CtCi
2.3 Implement an algorithm to delete a node in the middle (ie. any node
but the first and last node, not necessarily the exact middle) of a singly linked
list, given only access to that node.

Eg.
Input the node c from the linked list:
a->b->c->d->e->f

Result: nothing is returned, but the new linked list looks like
a->b->d->e->f
"""

def delete_middle_node(node):
    """
    To delete the middle node, we simply move the subsequent values i node forward.
    """
    if not node:
        return
    prev = None
    curr = node
    while curr.next is not None:
        if prev is not None:
            prev.value = curr.value
        prev = curr
        curr = curr.next
    prev.value = curr.value
    prev.next = None
    return

"""
Singly linked list implementation.

"""

class Node(object):
    """docstring for Node"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """docstring for LinkedList"""
    def __init__(self, value):
        self.head = Node(value)

    def insert_front(self, value):
        """
        Insert node at front of the list

        """
        node = Node(value)
        node.next = self.head
        self.head = node
        return

    def insert_back(self, value):
        """
        Insert node at back of the list

        """
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        node = Node(value)
        curr.next = node
        return

    def delete(self, value):
        """
        Delete the node which contains the value
        """
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    self.head = self.head.next
                    return
                prev.next = curr.next
                del curr
                break
            prev = curr
            curr = curr.next
        return

    def get_head(self):
        return self.head
        
    def print_list(self):
        curr = self.head
        while curr is not None:
            print curr.value,
            curr = curr.next
        print ""
        return

    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return False

if __name__ == '__main__':
    l_list = LinkedList('a')
    l_list.insert_back('b')
    l_list.insert_back('c')
    l_list.insert_back('d')
    l_list.insert_back('e')
    l_list.insert_back('f')
    head = l_list.get_head()
    curr = head
    nodes = []
    while curr is not None:
        nodes.append(curr)
        curr = curr.next
    delete_middle_node(nodes[4]) # delete 'e'
    curr = head
    while curr is not None:
        print curr.value,
        curr = curr.next
