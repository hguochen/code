"""
CtCi
8.3 A magic indedx in an array A[0...n-1] is defined to be an index such that A[1] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists,
in array A.

FOLLOW UP

What if the values are not distinct?
"""

def magic_index_brute(arr):
    """
    Time: O(n)
    Space: O(1)
    """
    if not arr:
        return -1
    for i in xrange(len(arr)):
        if arr[i] == i:
            return i
    return -1

def magic_index_optimized(arr):
    """
    Time: O(lgn)
    Space: O(1)
    """
    return binary_search(arr, 0, len(arr)-1)

def binary_search(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid:
        return binary_search(arr, mid+1, high)
    return binary_search(arr, low, mid-1)

if __name__ == '__main__':
    arr1 = [2,3,1,3,6,9]
    print magic_index_brute(arr1) # 3
    print magic_index_optimized(arr1) # 3