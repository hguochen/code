"""
CtCi
2.7 Given two singly linked lists, determine if the two lists intersect. Return
the intersecting node. Note that the intersection is defined based on reference,
not value. That is, if the kth node of the first linked list is the exact same node
(by reference) as the jth node of the second linked list, then they are intersecting.
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


def intersection(head1, head2):
    """
    For lists to have a intersecting node, they must have the same length starting
    from the intersecting node.
    So if the given 2 lists have different length, we can trim the longer list to have
    the same length as the short lists.
    Then we can just traverse both lists together looking for the intersecting node, and
    return if found

    Time: O(n)
    Space: O(1)
    where n is the size of the longer list, if they are not the same size. or the size of a list.
    """
    if not head1 or not head2:
        return None
    len1 = list_length(head1)
    len2 = list_length(head2)
    if len1 > len2:
        head1 = trim_by_length(head1, len1 - len2)
    elif len2 > len1:
        head2 = trim_by_length(head2, len2 - len1)

    curr1 = head1
    curr2 = head2
    while curr1 is not None:
        if curr1 == curr2:
            # found intersecting node
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next
    # no intersecting nodes
    return None

def trim_by_length(head, size):
    for i in xrange(size):
        head = head.next
    return head

def list_length(head):
    if not head:
        return 0
    curr = head
    size = 0
    while curr is not None:
        size += 1
        curr = curr.next
    return size

if __name__ == '__main__':
    pass