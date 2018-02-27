"""
Implementing a Stack data structure

"""


class Stack(object):
    """Stack Data Structure"""
    def __init__(self, stack=[]):
        super(Stack, self).__init__()
        self.stack = stack

    def print_stack(self):
        """
        time: O(1)
        """
        print self.stack

    def push(self, item):
        """
        time: O(1)
        """
        self.stack.append(item)

    def pop(self):
        """
        time: O(1)
        """
        return self.stack.pop()

    def top(self):
        """
        time: O(1)
        """
        if not self.stack:
            return
        return self.stack[-1]

def main():
    stack = Stack([1,2,3,4])
    stack.print_stack()
    stack.push(5)
    stack.print_stack()
    stack.push(6)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    print stack.top()


if __name__ == '__main__':
    main()