"""
CtCi
8.9 Implement an algorithm to print all valid(eg. properly opened and closed)
combinations of n pairs of parenthesis.

Example:
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
import copy

def parenthesis(n):
    """
    Time: O(n!)
    Space: O(n!)
    """
    if n < 1:
        return []
    paren = "()"
    result = []
    for i in xrange(1, n+1):
        if not result:
            result.append(paren)
            continue
        temp = generate_paren_sets(result, paren)
        result = copy.deepcopy(temp)
    return result

def generate_paren_sets(arr, paren):
    temp = []
    if not arr:
        return temp
    for res in arr:
        for i in xrange(len(res)):
            new_set = res[:i] + paren + res[i:]
            if new_set not in temp:
                temp.append(new_set)
    return temp


if __name__ == '__main__':
    print parenthesis(1)
    print parenthesis(2)
    print parenthesis(3)
    print parenthesis(4)
