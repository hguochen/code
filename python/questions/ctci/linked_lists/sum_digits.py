"""
CtCi
2.5 You have two numbers represented by a linked list, where each node contains
a single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

Follow up
Suppose the digits are stored in forward order. Repeat the above problem
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

def sum_digits(list_a, list_b):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of a / b. given that both lists are of the same length.
    
    Assume both lists are of the same length.

    Eg.
    Input: (7->1->6) + (5->9->2). That is 617+295
    Ouput: 2->1->9. That is 912
    """
    if not list_a:
        return list_b
    elif not list_b:
        return list_a
    carry = 0
    prev = None
    curr_a = list_a
    curr_b = list_b

    while curr_a is not None:
        temp = curr_a.value + curr_b.value + carry
        if temp >= 10:
            carry = 1
            temp %= 10
        else:
            carry = 0
        curr_a.value = temp
        prev = curr_a
        curr_a = curr_a.next
        curr_b = curr_b.next
    if carry == 1:
        prev.next = Node(1)
    return list_a

def sum_digits_2(list_a, list_b):
    """
    Time: O(n)
    Space: O(n)

    Eg.
    Input: (6->1->7) + (2->9->5). That is 617 + 295
    Ouput: (9->1->2) That is 912

    reverse the list. then use sum_digits function.
    reverse the result. then return.
    """
    new_a = reverse_list(list_a)
    new_b = reverse_list(list_b)
    result = sum_digits(new_a, new_b)
    return reverse_list(result)

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



if __name__ == '__main__':
    ll_a = LinkedList(7)
    ll_a.insert_back(1)
    ll_a.insert_back(6)
    list_a = ll_a.get_head()

    ll_b = LinkedList(5)
    ll_b.insert_back(9)
    ll_b.insert_back(2)
    list_b = ll_b.get_head()

    result = sum_digits(list_a, list_b)
    while result is not None:
        print result.value,
        result = result.next
    print

    ll_c = LinkedList(6)
    ll_c.insert_back(1)
    ll_c.insert_back(7)
    list_c = ll_c.get_head()

    ll_d = LinkedList(2)
    ll_d.insert_back(9)
    ll_d.insert_back(5)
    list_d = ll_d.get_head()

    result2 = sum_digits_2(list_c, list_d)
    while result2 is not None:
        print result2.value,
        result2 = result2.next
    print
