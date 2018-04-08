"""
CtCi
8.7 Write a method to compute all permutations of a string of unique characters.
"""

import copy

def permutations_without_dups(string):
    """
    Time: O(n!)
    Space: O(n!)
    take out a char from the string, permutate the rest of the string, then
    finally append the char to front of string.
    """
    if len(string) < 1:
        return
    str_list = list(string)
    return perm_util(str_list)

def perm_util(str_list):
    if len(str_list) < 1:
        return []
    elif len(str_list) == 1:
        return [str_list]
    result = []
    for i in xrange(len(str_list)):
        val = str_list[i]
        rem = str_list[:i] + str_list[i+1:]
        temp = perm_util(rem)
        for item in temp:
            result.append([val] + item)
    return result

def permutations_without_dups2(string):
    if len(string) < 1:
        return
    
    result = perm_util2(string)
    return result

def perm_util2(string):
    if len(string) < 1:
        return []
    elif len(string) == 1:
        return [string[0]]
    result = []
    for i in xrange(len(string)):
        el = string[i]
        rem = string[:i] + string[i+1:]
        temp = perm_util2(rem)
        for item in temp:
            result.append(el + item)
    return result

def permuations_backtracking(string):
    if len(string) < 1:
        return []
    result = []
    perm_util3(list(string), 0, len(string)-1, result)
    return result

def perm_util3(string, start, end, result):
    if start == end:
        result.append(copy.deepcopy(string))
        return
    for i in xrange(start, end+1):
        string[i], string[start] = string[start], string[i]
        perm_util3(string, start+1, end, result)
        string[i], string[start] = string[start], string[i]

def permutations_build_from_base(string):
    if len(string) < 1:
        return []
    result = []
    for i in xrange(len(string)):
        result = generate_permutations(string[i], result)
    return result

def generate_permutations(char, result):
    if len(result) < 1:
        result.append(char)
        return result
    temp_res = []
    for res in result:
        temp = []
        for i in xrange(0, len(res)):
            new_char = res[:i] + char + res[i:]
            temp.append(new_char)
        # put char at last index
        temp.append(res + char)
        temp_res.extend(temp)
    result = copy.deepcopy(temp_res)
    return result

if __name__ == '__main__':
    string1 = "abc"
    print permutations_without_dups(string1)
    print permutations_without_dups2(string1)
    print permuations_backtracking(string1)
    print permutations_build_from_base("abc")
