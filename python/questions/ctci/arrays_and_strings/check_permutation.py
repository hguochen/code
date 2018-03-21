"""
CtCi
1.2 Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(str1, str2):
    """
    Time: O(mn)
    Space: O(max(m, n))
    where m is the size of str1, n size of str2.
    """
    if not str1 or not str2:
        return False
    table = {}
    for value in str1:
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    for value in str2:
        if value not in table:
            return False
        else:
            table[value] -= 1
        if table[value] == 0:
            del table[value]
    return len(table) == 0

def check_permutation_with_sort(str1, str2):
    """
    Time: O(nlgn + mlgm)
    Space: O(n+m)
    where m is the size of str1, n size of str2
    """
    if not str1 or not str2 or len(str1) != len(str2):
        return False

    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    for i in xrange(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    str1 = "abc"
    str2 = "cba"

    str3 = "test"
    str4 = "estt"

    str5 = "testt"
    str6 = "estt"

    print check_permutation(str1, str2) # True
    print check_permutation(str3, str4) # True
    print check_permutation(str5, str6) # False

    print check_permutation_with_sort(str1, str2)
    print check_permutation_with_sort(str3, str4)
    print check_permutation_with_sort(str5, str6)
