"""
CtCi
2.1 Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""

def remove_dups(head):
    """
    put every item in a hash table. check and remove duplicates
    Time: O(n)
    Space: O(n)
    where n is the length of the linked list
    """
    if head is None:
        return
    table = {head.value: 1}
    prev = head
    curr = head.next
    while curr is not None:
        if curr.value not in table:
            table[curr.value] = 1
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next
    curr2 = head
    while curr2 is not None:
        print curr2.value,
        curr2 = curr2.next
    print
    return head

def remove_dups_2(head):
    """
    for each value, check if the rest of the list has duplicates
    Time: O(n^2)
    Space: O(1)
    """
    if head is None:
        return
    curr = head
    while curr is not None:
        prev = curr
        subsequent = curr.next
        while subsequent is not None:
            if subsequent.value == curr.value:
                prev.next = subsequent.next
            else:
                prev = subsequent
            subsequent = subsequent.next
        curr = curr.next
    curr2 = head
    while curr2 is not None:
        print curr2.value,
        curr2 = curr2.next
    print
    return head

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

if __name__ == "__main__":
    l_list = LinkedList(1)
    l_list.insert_back(3)
    l_list.insert_back(7)
    l_list.insert_back(4)
    l_list.insert_back(3)
    l_list.insert_back(2)
    l_list.insert_back(7)
    head = l_list.get_head()
    remove_dups(head)
    remove_dups_2(head)
