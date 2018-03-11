"""
Bubble Sort

Sort the array by repeatedly swapping adjacent elements if they are in the wrong order.

Time: O(n^2)
Space: O(1)
"""

def bubble_sort(array):
    if len(array) < 2:
        return array
    while True:
        swapped = False
        for i in xrange(1, len(array)):
            if array[i] < array[i-1]:
                swapped = True
                array[i], array[i-1] = array[i-1], array[i]
        if not swapped:
            break
    return array

if __name__ == "__main__":
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    print bubble_sort(arr1)
    print bubble_sort(arr2)
