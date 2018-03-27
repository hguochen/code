"""
CtCi
3.1 Describe how you could use a single array to implement three stacks
"""

class Index(object):
    def __init__(self, curr_index, min_index, max_index):
        self.curr_index = curr_index
        self.min_index = min_index
        self.max_index = max_index
        
class Stack(object):
    def __init__(self, size=30):
        self.stacks = [None] * size
        self.indexes = [Index(0, 0, 9), Index(10, 10, 19), Index(20, 20, 29)]

    def push(self, stack, item):
        if stack >= len(self.indexes):
            print "not a valid stack"
            return
        elif self.indexes[stack].curr_index > self.indexes[stack].max_index:
            print "stack", stack, "is full"
            return
        index = self.indexes[stack].curr_index
        self.stacks[index] = item
        self.indexes[stack].curr_index += 1
        return


    def pop(self, stack):
        if stack >= len(self.indexes):
            print "not a valid stack"
            return
        elif self.indexes[stack].curr_index < self.indexes[stack].min_index:
            print "stack", stack, "is empty"
            return
        self.indexes[stack].curr_index -= 1
        index = self.indexes[stack].curr_index
        value = self.stacks[index]
        self.stacks[index] = None
        return value

    def peek(self, stack):
        if stack >= len(self.indexes):
            print "not a valid stack"
            return
        index = self.indexes[stack].curr_index - 1
        return self.stacks[index]
        

    def is_empty(self, stack):
        if stack >= len(self.indexes):
            print "not a valid stack"
            return
        return self.indexes[stack].curr_index == self.indexes[stack].min_index


    def print_stack(self):
        print self.stacks

if __name__ == '__main__':
    stack = Stack()
    stack.push(1, 99)
    stack.push(1, 100)
    stack.push(1, 101)
    stack.print_stack()
    print stack.pop(1)
    stack.print_stack()
    print stack.pop(1)
    stack.print_stack()
    print stack.pop(1)
    stack.print_stack()