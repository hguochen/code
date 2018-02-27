"""
Implement two stacks in one array in such a way that neither stack overflows
unless the total number of elements in both stacks together is n.
push and pop operations should run in O(1) time.
"""

class TwoStack(object):
    """Implement two stacks in a single array"""
    def __init__(self, size=10):
        super(TwoStack, self).__init__()
        self.stack = [None] * size
        self.stack1_ptr = 0
        self.stack2_ptr = size - 1

    def push(self, stack, item):
        if self.stack1_ptr > self.stack2_ptr:
            print "Both stacks are full"
            return
        if stack == 1:
            self.stack[self.stack1_ptr] = item
            self.stack1_ptr += 1
        elif stack == 2:
            self.stack[self.stack2_ptr] = item
            self.stack2_ptr -= 1
        return

    def pop(self, stack):
        if self.stack1_ptr == 0 and self.stack2_ptr == len(self.stack) - 1:
            print "Both stacks are empty"
        elif self.stack1_ptr < 0:
            print "Stack 1 is empty"
        elif self.stack2_ptr == len(self.stack):
            print "Stack 2 is empty"

        if stack == 1:
            item = self.stack[self.stack1_ptr - 1]
            self.stack[self.stack1_ptr - 1] = None
            self.stack1_ptr -= 1
            return item
        elif stack == 2:
            item = self.stack[self.stack2_ptr + 1]
            self.stack[self.stack2_ptr + 1] = None
            self.stack2_ptr += 1
            return item

    def print_stack(self):
        print self.stack, self.stack1_ptr, self.stack2_ptr

def main():
    two_stack = TwoStack(15)
    two_stack.print_stack()
    two_stack.push(1, "apple")
    two_stack.print_stack()
    two_stack.push(1, "pear")
    two_stack.print_stack()
    two_stack.push(2, "orange")
    two_stack.print_stack()
    two_stack.push(2, "watermelon")
    two_stack.print_stack()
    print "popping"
    two_stack.pop(1)
    two_stack.print_stack()
    two_stack.pop(2)
    two_stack.print_stack()
    two_stack.pop(1)
    two_stack.print_stack()
    two_stack.pop(2)
    two_stack.print_stack()

if __name__ == '__main__':
    main()
