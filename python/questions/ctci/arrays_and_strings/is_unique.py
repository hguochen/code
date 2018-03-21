"""
CtCi 
1.1 Implement an algorithm to determine if a string has all the unique characters.
What if you cannot use additional data structures?

"""

def is_unique_using_hashtable(word):
    """
    Time: O(n)
    Space: O(n)
    where n is the word length
    """
    if not word:
        return False
    table = {}
    for i in xrange(len(word)):
        if word[i] not in table:
            table[word[i]] = None
        else:
            return False
    return True

def is_unique_using_sort(word):
    """
    Time: O(nlgn)
    Space: O(n)
    where n is the word length
    """
    chars = list(word)
    chars.sort()
    for i in xrange(1,len(chars)):
        if chars[i] == chars[i-1]:
            return False
    return True

if __name__ == '__main__':
    word1 = "Word"
    word2 = "Nootunique"

    print is_unique_using_hashtable(word1) # True
    print is_unique_using_hashtable(word2) # False

    print is_unique_using_sort(word1) # True
    print is_unique_using_sort(word2) # False
