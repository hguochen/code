"""
CtCi
8.4 Write a method to return all subsets of a set.
"""
import string
import copy

def power_set(arr):
    """
    Time: O(n2^n)
    Space: O(n2^n)
    where n is the size of the arr
    """
    result = []
    if not arr:
        return result
    # result will have 2^(num elements in array)
    size = 2**(len(arr))
    for i in xrange(size):
        # eg. bin(4) is 0b11
        mask = bin(i)[2:]
        # front pad with 0 until the mask is of same length as array
        mask = string.zfill(mask, len(arr))
        temp = []
        # loop through mask, if value is 1, put this array value into current result
        for j in xrange(len(mask)):
            if mask[j] == "1":
                temp.append(arr[j])
        result.append(temp)
    return result

def power_set_iterative(arr):
    """
    each power set is built up from the smaller subset
    Time: O(n2^n)
    Space: O(n2^n)
    """
    result = [[]]
    if not arr:
        return result
    for i in xrange(len(arr)):
        temp = copy.deepcopy(result)
        for item in temp:
            item.append(arr[i])
        result.extend(temp)
    return result

def power_set_recursive(arr):
    """
    Time: O(n2^n)
    Space: O(n2^n)
    """
    result = [[]]
    if not arr:
        return result
    power_set_recursive_util(arr, 0, result)
    return result

def power_set_recursive_util(arr, i, result):
    if i >= len(arr):
        return
    temp = copy.deepcopy(result)
    for item in temp:
        item.append(arr[i])
    result.extend(temp)
    power_set_recursive_util(arr, i+1, result)

if __name__ == '__main__':
    arr1 = ['a', 'b', 'c']
    print power_set(arr1)
    print power_set_iterative(arr1)
    print power_set_recursive(arr1)
