# Given an array of integers, find the first repeating element in it.

def first_repeating_element(array):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the array
    """
    if not array:
        return
    table = {}
    result = None
    for i in range(len(array)):
        if array[i] in table:
            if result is None:
                result = table[array[i]]
            elif table[array[i]] < result:
                result = table[array[i]]
        else:
            table[array[i]] = i
    return array[result]

if __name__ == '__main__':
    arr1 = [10, 5, 3, 4, 3, 5, 6]
    arr2 = [6, 10, 5, 4, 9, 120, 4, 6, 10]
    print first_repeating_element(arr1)
    print first_repeating_element(arr2)
