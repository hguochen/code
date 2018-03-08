"""
Implementation of max heap data structure.
"""

class MaxHeap(object):
    def __init__(self, heap=[]):
        self.heap = heap

    def find_max(self):
        return self.heap[1]

    def extract_max(self):
        result = self.heap.pop(1)
        self.build_max_heap()
        return result

    def insert(self, value):
        self.heap.append(value)
        self.build_max_heap()
        return

    def __parent(self, index):
        return index-1 / 2

    def __left(self, index):
        return 2 * index

    def __right(self, index):
        return 2 * index + 1

    def build_max_heap(self):
        """
        Time: O(nlgn)
        """
        for i in range(len(self.heap)/2, 0, -1):
            self.max_heapify(i)

    def max_heapify(self, index):
        """
        Maintains the max heap property.
        This method assumes left and right childrens of index are max heaps.
        But index element might be smaller than its children, so we float down this
        index element into the max heap so the subtree rooted at index i obeys the max heap property

        Time: O(lgn)
        """
        left = self.__left(index)
        right = self.__right(index)
        largest = index
        
        if left < len(self.heap) and self.heap[left] > self.heap[index]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            # swap the index element with the largest
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)
        return

    def print_heap(self):
        print self.heap


if __name__ == '__main__':
    heap = MaxHeap([4,1,3,2,16,9,10,14,8,7])
    heap.print_heap()
    print heap.extract_max()
    heap.print_heap()
    print heap.extract_max()
    heap.print_heap()
    print heap.extract_max()
    heap.print_heap()