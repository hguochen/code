# Given an array of pairs, find all symmetric pairs in it
# For example, a symmetric pair are (10, 20) and (20, 10)

def symmetric_pairs(array):
    """
    Time: O(n) where n is size of the array
    Space: O(n)
    """
    # check for boundary cases
    # init a dict
    # init result
    # loop through array
    #   check if the reverse 
    if not array:
        return
    table = {}
    result = []
    for item in array:
        key = (item[1], item[0])
        if key in table:
            result.append(item)
        else:
            table[item] = None
    return result


if __name__ == '__main__':
    arr1 = [(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]
    print symmetric_pairs(arr1)
