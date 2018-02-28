"""
Implement stack data structure with 2 queues.

"""

class Queue(object):
    """Queue Data Structure"""
    def __init__(self, queue=[]):
        super(Queue, self).__init__()
        self.queue = queue

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return
        return self.queue.pop(0)

    def peek_last(self):
        """return the last inserted element in the queue"""
        if not self.queue:
            return
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def print_queue(self):
        print self.queue

class Stack(object):
    """docstring for Stack"""
    def __init__(self):
        self.queue1 = Queue([])
        self.buffer = Queue([])

    def push(self, item):
        """
        Put item into queue 1.
        """
        self.queue1.enqueue(item)
        return

    def pop(self):
        """
        We want to pop the last element in queue1, so we keep popping queue1 items
        and put in queue2(acts as a holding container) until the last element in queue1.
        put the last element into a variable and return it.
        then we put queue2 items back into queue1.
        """
        if self.queue1.is_empty():
            return
        # move queue1 elements into buffer queue except for last element
        while True:
            value = self.queue1.dequeue()
            if not self.queue1.is_empty():
                self.buffer.enqueue(value)
            else:
                break
        # put elements in buffer queue back into queue 1
        while not self.buffer.is_empty():
            element = self.buffer.dequeue()
            self.queue1.enqueue(element)
        return value

    def top(self):
        """
        Look at the last element in queue1
        """
        if not self.queue1:
            return
        return self.queue1.peek_last()

    def print_stack(self):
        print "queue 1 is", self.queue1.print_queue()
        print "queue 2 is", self.buffer.print_queue()
            

def main():
    stack1 = Stack()
    stack1.push(1)
    stack1.push(3)
    stack1.push(5)
    stack1.push(7)
    stack1.print_stack()
    print stack1.pop()
    stack1.print_stack()
    print stack1.pop()
    stack1.print_stack()
    print stack1.pop()
    stack1.print_stack()
    print stack1.pop()
    stack1.print_stack()

if __name__ == '__main__':
    main()