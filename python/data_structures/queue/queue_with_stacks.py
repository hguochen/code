"""
Implement queue data structure with 2 stacks
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

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        """
        time: O(1)
        """
        if not self.stack:
            return
        return self.stack[-1]

class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        self.stack = Stack([])
        self.pop_stack = Stack([])

    def enqueue(self, value):
        self.stack.push(value)
        return

    def dequeue(self):
        """
        move all the elements from stack into pop_stack. return the top element.
        move all the top_stack elements back into the stack.
        """
        if self.stack.is_empty():
            return
        while not self.stack.is_empty():
            item = self.stack.pop()
            self.pop_stack.push(item)
        result = self.pop_stack.pop()
        while not self.pop_stack.is_empty():
            item = self.pop_stack.pop()
            self.stack.push(item)
        return result

    def print_queue(self):
        self.stack.print_stack()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()

if __name__ == '__main__':
    main()