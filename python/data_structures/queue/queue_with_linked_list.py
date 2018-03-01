"""
Implement a queue with a singly linked list

"""
from linked_lists.linked_list import LinkedList

class Queue(object):
    """docstring for Queue"""
    def __init__(self, value):
        super(Queue, self).__init__()
        self.queue = LinkedList(value)

    def enqueue(self, value):
        self.queue.insert_back(value)
        return
    
    def dequeue(self):
        curr = self.queue.get_head()
        if curr is None:
            return
        result = curr.value
        self.queue.delete(result)
        return result

    def print_queue(self):
        self.queue.print_list()


def main():
    queue = Queue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()
    print queue.dequeue()
    queue.print_queue()

if __name__ == '__main__':
    main()