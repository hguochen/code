"""
Heap sort

To sort the array in ascending order, use build_max_heap().
To sort the array in descending order, use build_min_heap().

Time: O(nlgn)
Space: O(1)
"""

def heapsort(array):
    if len(array) < 2:
        return array

    idx = len(array) - 1
    # O(n)
    build_max_heap(array, idx)
    # O(nlgn)
    while True:
        array[0], array[idx] = array[idx], array[0]
        idx -= 1
        if idx == 0:
            break
        # O(lgn)
        max_heapify(array, idx, 0)
    return array


def min_heapify(array, last_index, curr_index):
    left = 2 * curr_index + 1
    right = 2 * curr_index + 2

    smallest = curr_index
    if left <= last_index and array[smallest] > array[left]:
        smallest = left
    if right <= last_index and array[smallest] > array[right]:
        smallest = right

    if smallest != curr_index:
        array[smallest], array[curr_index] = array[curr_index], array[smallest]
        min_heapify(array, last_index, smallest)
    return

def max_heapify(array, last_index, curr_index):
    left = 2 * curr_index + 1
    right = 2 * curr_index + 2

    largest = curr_index
    if left <= last_index and array[largest] < array[left]:
        largest = left
    if right <= last_index and array[largest] < array[right]:
        largest = right
    if largest != curr_index:
        array[largest], array[curr_index] = array[curr_index], array[largest]
        max_heapify(array, last_index, largest)
    return


def build_max_heap(array, index):
    """
    build a max heap starting from 0 to index
    """
    for i in xrange(index/2, -1, -1):
        max_heapify(array, index, i)

def build_min_heap(array, index):
    """
    build a min heap starting from 0 to index
    """
    for i in xrange(index/2, -1, -1):
        min_heapify(array, index, i)

if __name__ == '__main__':
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    print heapsort(arr1)
    print heapsort(arr2)
    print heapsort(arr3)
