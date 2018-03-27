"""
CtCi
3.4 Implement a MyQueue class which implements a queue using two stacks
"""

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        return

    def dequeue(self):
        if len(self.stack1) < 1:
            return None
        while len(self.stack1) > 0:
            value = self.stack1.pop()
            self.stack2.append(value)
        result = self.stack2.pop()
        while len(self.stack2) > 0:
            value = self.stack2.pop()
            self.stack1.append(value)
        return result

    def peek(self):
        if len(self.stack1) < 1:
            return None
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
if __name__ == '__main__':
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()
