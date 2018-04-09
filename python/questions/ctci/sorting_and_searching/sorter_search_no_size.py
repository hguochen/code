"""
CtCi
10.4 You are given an array-like data structure. Listy which lacks a size method.
It does, however have an elementAt(i) method that returns the element at index i
in O(1) time. If i is beyond the bound of the data structure, it returns -1.(For 
this reason, the data structure only supports positive integers.) Given a Listy which contains
sorted, positive integers, find the index at which an element x occurs. If x occurs
multiple times, you may return any index.
"""

def search(arr, element):
    """
    Time: O(lgn)
    Space: O(1)
    """
    if arr.elementAt(0) == -1:
        return -1
    idx = 1
    while arr.elementAt(idx) != -1:
        idx *= 2
    return binary_search(arr, element, 0, idx)

def binary_search(arr, element, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr.elementAt(mid) == element:
        return mid
    elif arr.elementAt(mid) == -1 or element < arr.elementAt(mid):
        return binary_search(arr, element, low, mid-1)
    else:
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    arr1 = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]

    print search(arr1, 5) # 3