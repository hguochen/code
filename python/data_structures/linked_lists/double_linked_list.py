"""
Double linked list implementation
"""

class Node(object):
    """docstring for Node"""
    def __init__(self, value, prev=None, next=None):
        super(Node, self).__init__()
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):
    """docstring for DoubleLinkedList"""
    def __init__(self, value):
        self.head = Node(value)

    def insert_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        return

    def insert_back(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        node.prev = curr
        return

    def delete(self, value):
        if self.head is None:
            return
        prev = None
        curr = self.head
        while curr is not None:
            if curr.value == value:
                if prev is None:
                    new_head = self.head.next
                    if new_head is not None:
                        new_head.prev = None
                    self.head = new_head
                else:
                    if curr.next is not None:
                        curr.next.prev = prev
                    prev.next = curr.next
            prev = curr
            curr = curr.next
        return


    def find(self, value):
        curr = self.head
        if curr is None:
            return
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return

    def print_list(self):
        if self.head is None:
            return
        curr = self.head
        while curr is not None:
            print curr.value,
            curr = curr.next
        print ""
        return

def main():
    linked_list = DoubleLinkedList(1)
    linked_list.insert_back(2)
    linked_list.insert_back(3)
    linked_list.insert_back(4)
    linked_list.print_list()
    linked_list.delete(4)
    linked_list.print_list()

if __name__ == '__main__':
    main()