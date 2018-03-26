"""
CtCi
2.6 Implement a function to cehck if a linked list is a palindrome. 
"""
import copy

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

def is_palindrome(head):
    """
    Use a hash table.
    Time: O(n)
    Space: O(n)
    where n is the size of the linked list.
    """
    if not head:
        return False
    table = {}
    curr = head
    while curr is not None:
        if curr.value not in table:
            table[curr.value] = 1
        else:
            table[curr.value] += 1
        curr = curr.next
    for key in table.keys():
        if table[key] % 2 == 0:
            del table[key]
    return len(table) <= 1

def is_palindrome_2(head):
    """
    Reverse the list and check if they are the same.
    Time: O(n)
    Space: O(n)
    """
    if not head:
        return False
    reverse_head = reverse_list(copy.deepcopy(head))
    curr = head
    while curr is not None:
        # print curr.value, reverse_head.value
        if curr.value != reverse_head.value:
            return False
        reverse_head = reverse_head.next
        curr = curr.next
    return True

def reverse_list(head):
    if not head:
        return None
    prev = None
    curr = head
    next_node = curr.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = next_node
        if curr is None:
            break
        next_node = curr.next
    head = prev
    return head

def is_palindrome_3(head):
    """
    Using a stack.
    Time: O(n)
    Space: O(n)
    """
    if not head:
        return False
    curr = head
    size = 0
    while curr is not None:
        size += 1
        curr = curr.next
    stack = []
    curr = head
    while curr is not None:
        if len(stack) < size/2:
            stack.append(curr.value)
        else:
            break
        curr = curr.next
    if size % 2 == 1:
        curr = curr.next
    while curr is not None:
        if curr.value == stack[-1]:
            stack.pop()
        else:
            return False
        curr = curr.next
    return len(stack) == 0

def print_list(head):
    if not head:
        print
        return
    print head.value,
    print_list(head.next)

def is_palindrome_4(head):
    """
    Time: O(n)
    Space: O(n)
    """
    length = list_length(head)
    result = is_palindrome_recur(head, length)
    return result[1]

def is_palindrome_recur(head, length):
    if head is None or length <= 0:
        return [None, True]
    elif length == 1:
        return [head.next, True]
    [node, result] = is_palindrome_recur(head.next, length-2)
    if node is None or not result:
        return [node, result]
    result = head.value == node.value
    node = node.next
    return [node, result]
    
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
    l_list1 = LinkedList(1)
    l_list1.insert_back(3)
    l_list1.insert_back(5)
    l_list1.insert_back(3)
    l_list1.insert_back(1)
    head1 = l_list1.get_head()
    print_list(head1)
    print is_palindrome(head1)
    print is_palindrome_2(head1)
    print is_palindrome_3(head1)
    print is_palindrome_4(head1)