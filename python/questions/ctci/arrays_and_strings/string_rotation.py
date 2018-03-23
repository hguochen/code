"""
CtCi
1.9 Assume you have a method 'isSubstring' which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of
s1 using only one call to isSubstring(eg. "waterbottle" is a rotation of "erbottlewat").
"""
import unittest

def string_rotation(s1, s2):
    """
    Time: O(n) where n is the size of s2 string
    Space: O(1)
    """
    if len(s1) != len(s2) or not s1 or not s2:
        return False
    temp = s2 + s2
    return is_substring(s1, temp)

def is_substring(s1, s2):
    return s2.find(s1) != -1

class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [test_string1, test_string2, expected] in self.data:
            actual = string_rotation(test_string1, test_string2)
            self.assertEqual(actual, expected)
        
if __name__ =="__main__":
    unittest.main()