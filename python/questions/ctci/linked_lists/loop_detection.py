"""
CtCi
2.8 Given a circular linked list, implement an algorithm that returns the node at the beginning
of the loop.

Circular linked list: A(corrupt) linked list in which a node's next pointer points to an earlier node,
so as to make a loop in the linked list.

Eg.
Input: A -> B -> C -> D -> E -> C(the same C as earlier)
Output: C
"""

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

def loop_detection(head):
    """
    Tortise and hare strategy.

    1. tortise goes through 1 node at a time
    2. hare goes through 2 ndoes at a time
    3. if either tortise or hare hits a None, there's no loop,exit and return None
    4. if there is a loop, tortise and hare will meet at some point
    5. when tortise and hare meets, reset the hare to head node.
    6. now both tortise and hare move 1 node at a time.
    7. when tortise and hare meets again at a node, that node is the start of the loop.
    8. return the loop
    """
    if not head:
        return None
    tortise = head
    hare = head
    traversed = False
    # tortise move 1 node while hare moves 2 nodes
    while tortise is not None and hare is not None:
        # tortise and hare met again but not at the starting node
        if tortise == hare and traversed:
            break
        traversed = True
        tortise = tortise.next
        hare = hare.next
        if hare is not None:
            hare = hare.next
        else:
            # if none is found, means there's no loop. return None
            return None
    hare = head
    while hare is not None:
        if tortise == hare:
            return hare
        tortise = tortise.next
        hare = hare.next
    return None

def construct_circular_list(head):
    curr = head
    node = None
    while curr.next is not None:
        if curr.value == 'C':
            node = curr
        curr = curr.next
    curr.next = node
    return head

if __name__ == '__main__':
    a_list = LinkedList('A')
    a_list.insert_back('B')
    a_list.insert_back('C')
    a_list.insert_back('D')
    a_list.insert_back('E')
    head = a_list.get_head()
    head = construct_circular_list(head)
    print loop_detection(head).value