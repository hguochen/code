"""
Implementation of min heap data structure.
"""

class MinHeap(object):
    def __init__(self, heap=[]):
        heap.insert(0, None)
        self.heap = heap
        if len(self.heap) > 1:
            self.build_min_heap()

    def find_min(self):
        return self.heap[1]

    def extract_min(self):
        value = self.heap.pop(1)
        self.build_min_heap()
        return value

    def insert(self, value):
        self.heap.append(value)
        self.build_min_heap()
        return

    def build_min_heap(self):
        for i in range(len(self.heap)/2, 0, -1):
            self.min_heapify(i)
        return

    def min_heapify(self, index):
        left = self.__left(index)
        right = self.__right(index)
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.min_heapify(smallest)
        return

    def __parent(self, index):
        return index / 2

    def __left(self, index):
        return 2 * index

    def __right(self, index):
        return 2 * index + 1

    def print_heap(self):
        print self.heap


if __name__ == '__main__':
    heap = MinHeap([4,1,3,2,16,9,10,14,8,7])
    heap.print_heap()
    print heap.extract_min()
    heap.print_heap()
    print heap.extract_min()
    heap.print_heap()
    print heap.extract_min()
    heap.print_heap()