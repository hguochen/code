"""
CtCi
2.4 Write code to partition a linked list around a value x,  such that all nodes
less than x come before all nodes great than or equal to x. If x is contained within
the list, the values of x only need to be after the elements less than x(see below).
The partition element x can appear anywhere in the "right partition"; it does not need
to appear between the left and right partitions.
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

def partition(head, partition):
    """
    Create a new list to store smaller values, and a new list to store bigger values than partition.
    Loop through the list and insert the values accordingly into smaller or bigger list.
    Append the bigger list right after the smaller list.

    Time: O(n)
    Space: O(n)
    """
    if not head:
        return head
    less_list, more_list = None, None

    curr = head
    while curr is not None:
        if curr.value < partition:
            if not less_list:
                less_list = LinkedList(curr.value)
            else:
                less_list.insert_back(curr.value)
        else:
            if not more_list:
                more_list = LinkedList(curr.value)
            else:
                more_list.insert_back(curr.value)
        curr = curr.next
    if less_list is not None and more_list is not None:
        less_head = less_list.get_head()
        more_head = more_list.get_head()
        curr = less_head
        while curr.next is not None:
            curr = curr.next
        curr.next = more_head
        return less_head
    else:
        if less_list is None:
            return more_list.get_head()
        else:
            return less_list.get_head()

def partition_2(head, value):
    """
    Create a result list.
    For items less than value, put it at the front of the list.
    Items more than value, put it at the back of the list.

    Time: O(n)
    Space: O(n)
    """
    if not head:
        return head
    result = LinkedList(head.value)
    curr = head.next
    while curr is not None:
        if curr.value < value:
            result.insert_front(curr.value)
        else:
            result.insert_back(curr.value)
        curr = curr.next
    return result.get_head()


if __name__ == '__main__':
    l_list = LinkedList(3)
    l_list.insert_back(5)
    l_list.insert_back(8)
    l_list.insert_back(5)
    l_list.insert_back(10)
    l_list.insert_back(2)
    l_list.insert_back(1)
    head = l_list.get_head()
    result = partition(head, 5)
    result2 = partition_2(head, 5)
    curr = result
    while curr is not None:
        print curr.value,
        curr = curr.next
    print
    curr2 = result2
    while curr2 is not None:
        print curr2.value,
        curr2 = curr2.next
