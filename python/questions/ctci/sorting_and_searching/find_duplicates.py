"""
CtCi
10.8 You have an array with all the numbers from 1 to N, where N is at most 32,000.
The array may have duplicate entries and you do not know what N is. With only 4KB of
memory available, how would you print all duplicates elements in the array?

"""

def find_duplicates(arr):
    if not arr:
        return []
    result = []
    for i in xrange(len(arr)):
        val = abs(arr[i])
        if arr[val] > 0:
            arr[val] = 0 - arr[val]
        else:
            result.append(val)
    return result

if __name__ == '__main__':
    arr1 = [5, 1, 5, 3, 4, 3, 6] # 5, 3
    print find_duplicates(arr1)
