"""
CtCi
1.5 There are three types of edits that can be performed on strings:
- insert a character,
- remove a character,
- or replace a character.
Given two strings, write a function to check if they are one edit(or zero edits) away.
"""
import unittest

def one_away(test1, test2):
    """
    Time: O(2^(n+m))
    Space: O(max(n, m))
    where n is size of test1, m is size of test2
    """
    result = one_away_aux(test1, test2, len(test1)-1, len(test2)-1)
    print result
    return result <= 1

def one_away_aux(test1, test2, i, j):
    if i == -1:
        return j + 1
    elif j == -1:
        return i + 1
    if test1[i] == test2[j]:
        return one_away_aux(test1, test2, i-1, j-1)
    elif test1[i] != test2[j] and i == j: # replace case
        return one_away_aux(test1, test2, i-1, j-1) + 1
    # insert, delete case
    return min(one_away_aux(test1, test2, i-1, j), one_away_aux(test1, test2, i, j-1)) + 1

# solution 2
def one_away_2(test1, test2):
    """
    Time: O(n)
    Space: O(1)
    where n is the size of short string
    """
    if len(test1) == len(test2):
        return one_edit_replace(test1, test2)
    elif len(test1) + 1 == len(test2):
        return one_edit_insert(test1, test2)
    elif len(test1) - 1 == len(test2):
        return one_edit_insert(test2, test1)
    return False

def one_edit_replace(test1, test2):
    has_replaced = False
    for i in xrange(len(test1)):
        if test1[i] != test2[i]:
            if has_replaced:
                return False
            has_replaced = True
    return True

def one_edit_insert(test1, test2):
    i = 0
    j = 0
    while i < len(test1) and j < len(test2):
        if test1[i] != test2[j]:
            if i != j:
                # has more than 1 difference because:
                # the only difference is meant for insertion but since i and j index are different,
                # a replacement also has to be factored in. which makes for more than 1 edit
                return False
            # increment j because test2 string is the longer string here
            j += 1
        else:
            i += 1
            j += 1
    return True

class Test(unittest.TestCase):
    """
    Test Cases

    """
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away_2(test_s1, test_s2)
            print test_s1, test_s2, actual
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
