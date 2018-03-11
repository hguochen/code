"""
Quick sort

Picks an element as pivot and partitions given array around the picked pivot.
Ways to pick a pivot:
- always pick first element as pivot
- always pick last element as pivot
- pick a random element as pivot
- pick median as pivot

Time: O(nlgn)
Space: O(1)
"""

def quick_sort(array, low, high):
    if low < high:
        # patritioning index is now at the right place
        index = partition(array, low, high)
        quick_sort(array, low, index-1)
        quick_sort(array, index+1, high)
    return array

def partition(array, low, high):
    pivot = array[high]
    smaller = low - 1

    for i in xrange(low, high):
        if array[i] <= pivot:
            smaller += 1
            array[i], array[smaller] = array[smaller], array[i]
    array[smaller+1], array[high] = array[high], array[smaller+1]
    return smaller + 1

if __name__ == '__main__':
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    print quick_sort(arr1, 0, len(arr1)-1)
    print quick_sort(arr2, 0, len(arr2)-1)
    print quick_sort(arr3, 0, len(arr3)-1)
