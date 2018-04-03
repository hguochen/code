"""
https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

Generate all permutation of a set in python
"""
import copy

def permutation_backtracking(items, start, end, result):
    """
    Time: O(n!)
    Space: O(n!)
    where n is the size of items
    """
    if start == end:
        result.append(copy.deepcopy(items))
        return
    for i in xrange(start, end+1):
        items[start], items[i] = items[i], items[start]
        permutation_backtracking(items, start+1, end, result)
        items[start], items[i] = items[i], items[start]
    return

def permutation_extraction(items):
    """
    One by one extract all elements, place them at first position and recur for the remaining list.
    Time: O(n!)
    Space: O(n!)
    """
    if len(items) < 1:
        return []
    elif len(items) == 1:
        return [items]
    result = []
    for i in xrange(len(items)):
        val = items[i]
        rem_items = items[:i] + items[i+1:]
        perms = permutation_extraction(rem_items)
        for perm in perms:
            result.append([val] + perm)
    return result

if __name__ == '__main__':
    items1 = ['A', 'B', 'C']
    items2 = [1, 2, 3, 4]
    result1 = []
    permutation_backtracking(items1, 0, len(items1) - 1, result1)
    print permutation_extraction(items1)
    print result1

    result2 = []
    permutation_backtracking(items2, 0, len(items1) - 1, result2)
    print permutation_extraction(items2)
    print result2