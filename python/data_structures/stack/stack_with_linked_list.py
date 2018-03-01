"""
Implement a stack with a singly linked list
"""
from linked_lists.linked_list import LinkedList

class Stack(object):
    """docstring for Stack"""
    def __init__(self, value):
        super(Stack, self).__init__()
        self.stack = LinkedList(value)

    def push(self, value):
        self.stack.insert_front(value)

    def pop(self):
        curr = self.stack.get_head()
        value = curr.value
        self.stack.delete(value)
        return value

    def print_stack(self):
        self.stack.print_list()

def main():
    stack = Stack(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print stack.pop()
    stack.print_stack()
    print stack.pop()
    stack.print_stack()

if __name__ == '__main__':
    main()