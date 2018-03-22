"""
CtCi
1.6 Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string 'aabcccccaaa' would become 'a2b1c5a3'.
If the compressed string would not become smaller than the original string, your
method should return the original string. You can assume the string has only uppercase
and lowercase letters(a-z)
"""

import unittest

def string_compression(string):
    """
    Time: O(n)
    Space: O(n)
    """
    if not string:
        return string
    histogram = []
    for i in xrange(len(string)):
        if not histogram:
            histogram.append([string[i], 1])
            continue
        if histogram[-1][0] == string[i]:
            histogram[-1][1] += 1
        else:
            histogram.append([string[i], 1])
    result = ""
    for item in histogram:
        result += item[0] + str(item[1])
    if len(string) < len(result):
        return string
    return result

def string_compression_2(string):
    """
    Modify string with only a result string
    Time: O(n)
    Space: O(n)
    """
    if not string:
        return string
    result = ""
    prev = ""
    count = 0
    for i in xrange(len(string)):
        if not prev:
            prev = string[i]
            count += 1
            continue
        if prev == string[i]:
            count += 1
        else:
            result += prev + str(count)
            prev = string[i]
            count = 1
    if prev:
        result += prev + str(count)
    if len(result) <= len(string):
        return result
    return string

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [string, expected] in self.data:
            actual = string_compression_2(string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
