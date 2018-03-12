"""
Radix Sort
https://www.geeksforgeeks.org/radix-sort/

Uses bucket sort as a sub routine.

Time: O(nk) where n is the number of elements in array, k is the max_digit value
Space: O(n)
"""

def radix_sort(array, max_digit):
    if len(array) < 2:
        return array
    buckets = [[] for _ in range(10)]
    divide, mod = 1, 10
    result = array[:]

    i = 1
    while i <= max_digit:
        for value in result:
            index = (value / divide) % mod
            buckets[index].append(value)
            buckets[index].sort()
        divide *= 10
        # flatten into result list
        result = [value for sublist in buckets for value in sublist]
        buckets = [[] for _ in range(10)]
        i += 1
    return result

if __name__ == '__main__':
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    arr4 = [1, 4, 1, 2, 7, 5, 2]
    arr5 = [170, 45, 75, 90, 802, 24, 2, 66]
    print radix_sort(arr1, 2)
    print radix_sort(arr2, 2)
    print radix_sort(arr3, 2)
    print radix_sort(arr4, 1)
    print radix_sort(arr5, 3)
