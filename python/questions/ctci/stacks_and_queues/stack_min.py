"""
CtCi
3.2 How would you design a stack which, in addition to push and pop, has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time.

On each layer of the stack, store the min value up to this layer.

    ------------------
min | 5, 3, 3
curr| 5, 3, 4
    ------------------
"""

class Item(object):
    def __init__(self, value, min_value):
        self.value = value
        self.min_value = min_value

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        item = Item(value, value)
        if len(self.stack) > 0 and self.stack[-1].min_value < value:
                item.min_value = self.stack[-1].min_value
        self.stack.append(item)
        return

    def pop(self):
        if len(self.stack) < 1:
            return
        item = self.stack.pop()
        return item.value

    def peek(self):
        if len(self.stack) < 1:
            return
        return self.stack[-1].value

    def min_value(self):
        if len(self.stack) < 1:
            return
        return self.stack[-1].min_value

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        for item in self.stack:
            print "[" + str(item.value), str(item.min_value) + "]"
        print

if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    stack.print_stack()
    stack.push(5)
    stack.print_stack()
    stack.push(8)
    stack.print_stack()
    stack.push(1)
    stack.print_stack()
    stack.push(12)
    stack.print_stack()

    print stack.peek()
    print stack.min_value()
