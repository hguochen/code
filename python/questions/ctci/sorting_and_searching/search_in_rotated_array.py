"""
CtCi
10.3 Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the array was originally
sorted in increasing order.

Eg.
Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8(the index of 5 in the array)

"""

def search(array, element):
    """
    Time: O(nlgn) worse case O(n)
    Space: O(1)
    """
    if len(array) < 1:
        return -1
    return binary_search(array, element, 0, len(array)-1)

def binary_search(array, element, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if array[mid] == element:
        return mid
    if array[low] < array[mid]: # left is normally ordered
        if array[low] <= element and element < array[mid]: # search left
            return binary_search(array, element, low, mid-1)
        else:
            return binary_search(array, element, mid+1, high)
    elif array[mid] < array[high]: # right is normally ordered
        if array[mid] < element and element <= array[high]: # search right
            return binary_search(array, element, mid+1, high)
        else:
            return binary_search(array, element, low, mid-1)
    elif array[low] == array[mid]: # left to mid is all repeats
        if array[mid] != array[high]: # right is different, search it
            return binary_search(array, element, mid+1, high)
        else: # both left and right are the same, we have to search both halves
            res = binary_search(array, element, low, mid-1) # search left
            if res == -1:
                return binary_search(array, element, mid+1, high)
            return res
    return -1



if __name__ == '__main__':
    arr1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

    print search(arr1, 15)
    print search(arr1, 16)
    print search(arr1, 19)
    print search(arr1, 20)
    print search(arr1, 25)
    print search(arr1, 1)
    print search(arr1, 3)
    print search(arr1, 4)
    print search(arr1, 5)
    print search(arr1, 7)
    print search(arr1, 10)
    print search(arr1, 14)
