"""
Implementing a queue data structure

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

    def print_queue(self):
        print self.queue

def main():
    assert 2 == 2
    queue = Queue([1,2,3,4])
    queue.enqueue(5)
    queue.print_queue()
    queue.enqueue(6)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()

if __name__ == '__main__':
    main()