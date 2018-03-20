"""
https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

"""

def has_subset_sum(values, total):
    """
    Hash Table solution.
    Time: O(n)
    Space: O(n)
    """
    if len(values) < 1:
        return False
    table = {}
    for value in values:
        if value not in table:
            table[total - value] = value
        else:
            print table[value], value
            return True
    return False

def has_subset_sum_recursion(values, index, total):
    """
    DP solution.
    Time: O(2^n)
    Space: O(n)
    """
    if total == 0:
        return True
    if index == -1 and total != 0:
        return False

    if values[index] > total:
        # value is bigger than total, going to negative is futile since there are no -ve values in list
        # we can just omit this value
        return has_subset_sum_recursion(values, index-1, total)
    # else check if sum can be obtained
    # 1. exclude last element
    # 2. include last element
    return has_subset_sum_recursion(values, index-1, total) or has_subset_sum_recursion(values, index-1, total-values[index])

def has_subset_sum_dp(values, total):
    """
    TODO: DP solution
    Time: O(n^2)
    Space: O(n^2)
    """
    if total == 0:
        return True
    elif total != 0 and len(values) == 0:
        return False
    table = [[None for _ in range(len(values))] for _ in range(len(values))]

    for row in range(len(table)):
        for col in range(len(table[row])):
            if row == col:
                continue
            if values[row] + values[col] == total:
                return True
            else:
                table[row][col] = False
    return False

if __name__ == '__main__':
    values1 = [3, 34, 4, 12, 5, 2]
    print has_subset_sum(values1, 9)
    print has_subset_sum_recursion(values1, len(values1)-1, 9)
    print has_subset_sum_dp(values1, 9)