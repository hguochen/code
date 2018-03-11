"""
Insertion sort
Time: O(n^2) where n is the number of elements to be sorted
Space: O(1)
"""

def insertion_sort(array):
    if len(array) < 2:
        return array
    # partition array by last sorted index
    last_sorted = 0
    for i in xrange(1, len(array)):
        pos = i
        # loop through from last_sorted element into first element
        for j in xrange(last_sorted, -1, -1):
            # if current element is less than the element on its left, swap them
            # update current element to point to the swapped index
            # else element at pos is at its rightful position
            if array[pos] < array[j]:
                array[j], array[pos] = array[pos], array[j]
                pos = j
            else:
                break
        # elements on right of last_sorted index is now sorted, we update the last_sorted index
        last_sorted += 1
    return array

def insertion_sort_2(array):
    if len(array) < 2:
        return array
    for i in xrange(1,len(array)):
        value = array[i]
        # move elements of array[0...i-1], that are greater than value, 1 position to the right of their
        # current position
        j = i-1
        while j >= 0 and value < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = value
    return array

if __name__ == "__main__":
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    print insertion_sort(arr1)
    print insertion_sort_2(arr1)

    print insertion_sort(arr2)
    print insertion_sort_2(arr2)
