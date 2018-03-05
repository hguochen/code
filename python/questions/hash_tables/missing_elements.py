# Given an array of distinct elements and a range (low, high), find all the
# numbers that are in range, but not in array.


def missing_elements(array, boundary):
    """
    Time: O(n + m) where n is the size of the array, m is the number of elements defined by boundary
    Space: O(n)
    """
    if not array or not boundary:
        return []
    # put array elements into a dict.
    # loop through boundary range
    #   if current element is in dict, skip
    #   else put in result
    table = {}
    for val in array:
        table[val] = None
    result = []
    for i in range(boundary[0], boundary[1]+1):
        if i not in table:
            result.append(i)
    return result


if __name__ == '__main__':
    arr1 = [10,12,11,15]
    range1 = (10, 15)
    print missing_elements(arr1, range1)

    arr2 = [1,14,11,51,15]
    range2 = (50, 55)
    print missing_elements(arr2, range2)

    arr3 = [1, 3, 5, 4]
    range3 = (1, 10)
    print missing_elements(arr3, range3)
