"""
CtCi
1.4 Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

Assume case insensitive
"""

import unittest

def palindrome_permutation(string):
    """
    Time: O(n)
    Space: O(n)
    """
    if not string:
        return False
    temp = string.strip().lower()
    return has_palindrome_chars(temp)

def has_palindrome_chars(string):
    """
    string has palindrome chars if every char is in pairs or if there's only 1 odd char.
    Time: O(n)
    Space: O(n)
    where n is the size of the string
    """
    table = {}
    for i in xrange(len(string)):
        if string[i] == " ":
            continue
        elif string[i] not in table:
            table[string[i]] = 1
        else:
            table[string[i]] += 1

    for key in table.keys():
        if table[key] % 2 == 0:
            del table[key]

    return is_max_one_odd(table)

def is_max_one_odd(table):
    if not table:
        return True
    has_odd = False
    for key in table.keys():
        if table[key] % 2 == 1:
            if has_odd:
                return False
            else:
                has_odd = True
    return True

class Test(unittest.TestCase):
    """
    Test Cases
    """
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)
    ]

    def test_palindrome_permutation(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation(test_string)
            self.assertEqual(actual, expected)

        
if __name__ == '__main__':
    unittest.main()
    # data1 = 'no x in nixon'
    # print palindrome_permutation(data1)