"""
Binary search algorithm
Time: O(lgn)
Space: O(1)
"""

def binary_search(array, value):
    """
    Returns the index at which value resides in the array.
    """
    if len(array) < 1:
        return -1
    return binary_search_util(array, value, 0, len(array)-1)

def binary_search_util(array, value, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if array[mid] == value:
        return mid
    elif value < array[mid]:
        return binary_search_util(array, value, low, mid-1)
    else:
        return binary_search_util(array, value, mid+1, high)

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 10, 12]
    arr2 = [11, 12, 22, 25, 64]
    arr3 = [3, 9, 10, 27, 38, 43, 82]
    arr4 = [1, 1, 2, 2, 4, 5, 7]
    arr5 = [2, 24, 45, 66, 75, 90, 170, 802]

    print binary_search(arr1, 4) # 3
    print binary_search(arr1, 34) # -1
    print binary_search(arr2, 25) # 3
    print binary_search(arr3, 3)
    print binary_search(arr3, 9)
    print binary_search(arr3, 10)
    print binary_search(arr3, 27)
    print binary_search(arr3, 38)
    print binary_search(arr3, 43)
    print binary_search(arr3, 82)
