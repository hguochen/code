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
