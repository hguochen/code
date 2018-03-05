# Find whether an array is subset of another array
# Given 2 arrays, find whether an array is a subset of another.
# Both arrays are not in sorted order. 
# There can be repeated values in both arrays

def is_subarray(arr1, arr2):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the longer array
    """
    if not arr1:
        return False
    elif not arr2:
        return True
    table = {}
    for item in arr1:
        if item not in table:
            table[item] = 1
        else:
            table[item] += 1
    for item in arr2:
        if item not in table:
            return False
        else:
            if table[item] == 1:
                del table[item]
            else:
                table[item] -= 1
    return True

if __name__ == '__main__':
    arr1 = [11,1,13,21,3,7]
    arr2 = [11,3,7,1]
    arr3 = [1,2,3,4,5,6]
    arr4 = [1,2,4]
    arr5 = [10,5,2,23,19]
    arr6 = [19,5,3]
    print is_subarray(arr1, arr2)
    print is_subarray(arr3, arr4)
    print is_subarray(arr5, arr6)
