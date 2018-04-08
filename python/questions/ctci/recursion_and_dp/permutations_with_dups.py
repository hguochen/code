"""
CtCi
8.8 Write a method to compute all permutations of a string whose characters are not necessarily
unique. The list of permutations should not have duplicates.
"""
import copy

def permutations_with_dups(string):
    """
    Time: O(n!)
    Space: O(n!)
    where n is the size of string
    """
    if len(string) < 1:
        return []
    result = []
    perm_util(list(string), 0, len(string)-1, result)
    return result

def perm_util(arr, start, end, res):
    if start == end and arr not in res:
        res.append(copy.deepcopy(arr))
        return
    for i in xrange(start, end+1):
        arr[i], arr[start] = arr[start], arr[i]
        perm_util(arr, start+1, end, res)
        arr[i], arr[start] = arr[start], arr[i]

def permutations_with_dups2(string):
    if len(string) < 1:
        return []
    result = []
    table = build_freq_table(string)
    perm_util2(table, "", len(string), result)
    return result

def perm_util2(table, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return
    # try remaining letters for next char, and generate remaining permutations
    for char in table.keys():
        if table[char] > 0:
            table[char] -= 1
            perm_util2(table, prefix + char, remaining - 1, result)
            table[char] += 1

def build_freq_table(string):
    table = {}
    if len(string) < 1:
        return table
    for char in string:
        if char in table.keys():
            table[char] += 1
        else:
            table[char] = 1
    return table

if __name__ == '__main__':
    str1 = "abc"
    str2 = "abb"
    print permutations_with_dups(str1)
    print permutations_with_dups(str2)
    print permutations_with_dups2(str1)
    print permutations_with_dups2(str2)