# Given an array and a number x, determine whether or not there exists two elements in
# the array whose sum is exactly x

def has_sum_to_x(arr, x):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of given array
    """
    assert isinstance(x, (int, long))
    if len(arr) < 2:
        return False
    table = {}
    for num in arr:
        second_value = x - num
        if num in table:
            return num, second_value
        else:
            table[second_value] = num
    return False

if __name__ == '__main__':
    arr = [1, 4, 45, 6, 10, -8]
    x = 16
    print has_sum_to_x(arr, x)