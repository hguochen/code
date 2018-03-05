# Given an array of integers, and a number 'sum', find the number of pairs of integers
# in the array whose sum is equal to number 'sum'.

def sum_pairs(array, target):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the array
    """
    if not array:
        return []
    # init table
    # init result
    # loop through array
    #   if curr value in table, put set into result
    #   else insert key(target-curr): value: curr
    table = {}
    result = []
    for val in array:
        if val in table:
            table[val] += 1
        else:
            table[val] = 1
    for val in array:
        if target-val in table:
            result.append((val, target-val))
            table[val] -= 1
            if table[val] == 0:
                del table[val]
    return result

if __name__ == '__main__':
    arr1 = [1,5,7,-1]
    sum1 = 6
    print sum_pairs(arr1, sum1)

    arr2 = [1,5,7,-1,5]
    sum2 = 6
    print sum_pairs(arr2, sum2)

    arr3 = [1,1,1,1]
    sum3 = 2
    print sum_pairs(arr3, sum3)

    arr4 = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
    sum4 = 11
    print sum_pairs(arr4, sum4)
