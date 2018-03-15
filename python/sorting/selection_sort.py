"""
Selection sort

Sorts an array by repeatedly finding the minimum element from unsorted part and put it at the beginning

Time: O(n^2)
Space: O(1)
"""

def selection_sort(array):
    if len(array) < 2:
        return array
    unsorted = 0
    for i in xrange(len(array)):
        min_index = i
        min_value = array[i]
        j = i+1
        while j < len(array):
            if array[j] < min_value:
                min_index = j
                min_value = array[j]
            j += 1
        array[unsorted], array[min_index] = array[min_index], array[unsorted]
        unsorted += 1
    return array

def selection_sort_recursive(array, start, end):
    """
    Recursive implementation of selection sort
    """
    if start >= end:
        return
    index = min_index(array, start, end)

    temp = array[start]
    array[start] = array[index]
    array[index] = temp
    selection_sort_recursive(array, start+1, end)
    return array

def min_index(arr, start, end):
    min_index = start
    for i in xrange(start+1, end+1):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index
        
if __name__ == "__main__":
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    print selection_sort(arr1)
    print selection_sort(arr2)
    print selection_sort_recursive(arr1, 0, len(arr1)-1)
    print selection_sort_recursive(arr2, 0, len(arr2)-1)
