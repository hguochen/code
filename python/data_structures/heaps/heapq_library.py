# https://docs.python.org/2/library/heapq.html
import heapq

if __name__ == '__main__':
    arr = [4,1,3,2,16,9,10,14,8,7]
    
    # transform a list into a heap, in-place, in linear time
    heapq.heapify(arr)

    # push the value onto the heap, maintaining the heap invariant
    heapq.heappush(arr, 54)
    heapq.heappush(arr, 86)
    print arr

    # pop and return the smallest item from the heap. If heap is empty, IndexError is raised.
    print heapq.heappop(arr)

    # access the smallest item without popping it.
    print arr[0]

    # pop and return the smallest item from the heap and also push the new item onto heap.
    # the heap size doesn't change
    heapq.heapreplace(arr, 384)

    # return a list with the n largest elements from the dataset defined by iterable.
    # does NOT pop these elements
    print heapq.nlargest(3, arr)
    print arr

    # return a list with the n smallest elements from the dataset defined by iterable
    # does NOT pop these elements
    print heapq.nsmallest(3, arr)
    print arr
