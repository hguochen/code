"""
Given a string, the task is to find maximum consecutive repeating character in string.

Note : We do not need to consider overall count, but the count of repeating that appear at one place.

Examples:

Input : str = "geeekk"
Output : e

Input : str = "aaaabbcbbb"
Output : a
"""

def max_repeating_character(str1):
    """
    Time: O(n)
    Space: O(1)
    """
    if not str1:
        return ""
    max_count = 0
    result = str1[0]

    curr_count = 1
    for i in xrange(1,len(str1)):
        if str1[i] == str1[i-1]:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count
                result = str1[i-1]
            curr_count = 1
    return result

if __name__ == '__main__':
    str1 = "geeekk"
    str2 = "aaaabbcbbb"
    str3 = "aaaabbaaccde"

    print max_repeating_character(str1)
    print max_repeating_character(str2)
    print max_repeating_character(str3)
