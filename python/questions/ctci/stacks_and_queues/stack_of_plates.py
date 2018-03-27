"""
CtCi
3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might
topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold, Implement a data structure SetOfStacks
that mimics this. SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack(that is, pop() should return the same values as it would if there were
just a single stack).

FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack
"""

class SetOfStack(object):
    def __init__(self, threshold=5):
        self.stacks = [[]]
        self.curr_stack = 0
        self.threshold = threshold

    def push(self, item):
        if len(self.stacks[self.curr_stack]) >= self.threshold:
            self.stacks.append([item])
            self.curr_stack += 1
            return
        self.stacks[self.curr_stack].append(item)
        return

    def pop(self):
        if self.curr_stack == 0 and len(self.stacks[self.curr_stack]) < 1:
            print "stack is empty"
            return
        elif len(self.stacks[self.curr_stack]) < 1:
            self.stacks.pop()
            self.curr_stack -= 1
        return self.stacks[self.curr_stack].pop()


    def peek(self):
        if self.curr_stack == 0 and len(self.stacks[self.curr_stack]) < 1:
            print "stack is empty"
            return
        return self.stacks[self.curr_stack]

    def is_empty(self):
        if self.curr_stack != 0:
            return False
        return len(self.stacks[self.curr_stack]) < 1

    def print_stack(self):
        for stack in self.stacks:
            print stack
        return
        

if __name__ == '__main__':
    stack = SetOfStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.print_stack()
    print stack.pop()
    stack.print_stack()
    print stack.pop()
    stack.print_stack()
    print stack.pop()
    stack.print_stack()
    print stack.pop()
    stack.print_stack()