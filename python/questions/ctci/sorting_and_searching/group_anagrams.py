"""
CtCi
10.2 Write a method to sort an array of strings so that all the anagrams are next to each other.
"""

def sort_strings(arr):
    """
    hash table to order elements
    key: value
    string: [anagrams of the string]

    Time: O(mnlgn)
    Space: O(m)
    where m is size of array, n is size of longest word in array
    """
    if not arr:
        return []
    table = {}
    for item in arr:
        base = sort_chars(item)
        anagram = "".join(base)
        if anagram in table:
            table[anagram].append(item)
        else:
            table[anagram] = [item]
    result = []
    for key in table.keys():
        result.extend(table[key])
    return result

def sort_chars(chars):
    """
    mergesort
    Time: O(nlgn)
    Space: O(1)
    """
    arr = mergesort(list(chars), 0, len(chars)-1)
    return "".join(arr)

def mergesort(arr, low, high):
    if low < high:
        mid = (low + high) / 2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    temp = arr[:]
    left_i = low
    right_i = mid + 1
    idx = low

    while left_i <= mid and right_i <= high:
        if temp[left_i] < temp[right_i]:
            arr[idx] = temp[left_i]
            left_i += 1
        else:
            arr[idx] = temp[right_i]
            right_i += 1
        idx += 1
    while left_i <= mid:
        arr[idx] = temp[left_i]
        left_i += 1
        idx += 1

    while right_i <= high:
        arr[idx] = temp[right_i]
        right_i += 1
        idx += 1
    return

def sort_strings2(arr):
    """
    Time: O(mn)
    Space: O(m)
    where m is the size of array, n the size of longest string in array
    """
    if not arr:
        return []
    table = {}
    for item in arr:
        anagram_key = get_anagram_key(item)
        if anagram_key in table:
            table[anagram_key].append(item)
        else:
            table[anagram_key] = [item]
    result = []
    for key in table.keys():
        result.extend(table[key])
    return result

def get_anagram_key(chars):
    """
    Time: O(n)
    Space: O(1)
    """
    if not chars:
        return ""
    freq_table = [0 for _ in range(26)]
    for char in chars:
        idx = ord(char) - 97
        freq_table[idx] += 1
    result = ""
    for i in range(len(freq_table)):
        if freq_table[i] != 0:
            result += chr(i+97) + str(freq_table[i])
    return result


if __name__ == '__main__':
    arr1 = ["cat", "dog", "tac", "god", "act"]
    print sort_strings(arr1)
    print sort_strings2(arr1)
