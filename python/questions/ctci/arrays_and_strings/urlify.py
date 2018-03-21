"""
CtCi
1.3 Write a method to replace all spaces in a string with '%20'. You may assume
that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string.
"""

def urlify(url):
    """
    Time: O(n)
    Space:O(n)
    """
    if not url:
        return ""
    stripped = url.strip()
    result = ""
    for i in xrange(len(stripped)):
        if stripped[i] == " ":
            result += '%20'
        else:
            result += stripped[i]
    return result

def urlify_in_place(url):
    """
    Time: O(n)
    Space: O(1)
    """
    if not url:
        return ""
    result = url.strip()
    delimiter = "%20"
    i = len(result) - 1
    while i >= 0:
        if result[i] == " ":
            result = result[:i] + delimiter + result[i+1:]
        i -= 1
    return result

if __name__ == "__main__":
    url1 = "Mr John Smith    "

    print urlify(url1)
    print urlify_in_place(url1)
