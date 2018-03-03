"""
Implementation of direct address table with singly linked list
"""
from linked_lists.linked_list import *

class DirectAddressTable(object):
    """docstring for DirectAddressTable"""
    def __init__(self, size):
        super(DirectAddressTable, self).__init__()
        self.table = [None for _ in range(size)]

    def insert(self, key, value):
        if key >= len(self.table):
            print "Given key is larger than size of table"
            return
        if self.table[key] is None:
            self.table[key] = LinkedList(value)
        else:
            curr = self.table[key]
            node = Node(value)
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        return

    def delete(self, key):
        """
        Remove all of the values identified by the given key
        """
        self.table[key] = None
        return

    def find(self, key):
        if self.table[key]:
            return self.table[key].value

    def print_table(self):
        print self.table

def main():
    table = DirectAddressTable(10)
    table.print_table()

if __name__ == '__main__':
    main()
        