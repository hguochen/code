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
        
if __name__ == "__main__":
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    print selection_sort(arr1)
    print selection_sort(arr2)
