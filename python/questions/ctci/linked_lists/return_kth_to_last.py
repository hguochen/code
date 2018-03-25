"""
CtCi
2.2 Implement an algorithm to find the kth to last element of a singly linked list.

0 to last -> last element
1 to last -> last second element
2 to last -> last third element
"""

def kth_to_last(head, k):
    """
    Time: O(n)
    Space: O(1)
    where n is the size of the linked list.

    Make a first pass of the list to count the length.
    length - k = number of times to traverse to

    """
    if not head:
        return
    curr = head
    last_index = -1
    while curr is not None:
        last_index += 1
        curr = curr.next
    run_times = last_index - k
    result = head
    for i in xrange(0,run_times):
        result = result.next
    return result.value

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
    l_list = LinkedList(1)
    l_list.insert_back(5)
    l_list.insert_back(2)
    l_list.insert_back(4)
    l_list.insert_back(3)
    head = l_list.get_head()
    print kth_to_last(head, 0) # 3
    print kth_to_last(head, 1) # 4
    print kth_to_last(head, 2) # 2
    print kth_to_last(head, 3) # 5
    print kth_to_last(head, 4) # 1
