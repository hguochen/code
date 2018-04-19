"""
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

corner cases:
1. array is empty
2. array is not array object
3. array does not contain integers # assume array all contain integers
4. target is not a number
5. result not found

APPROACH
1. hash table
- loop through array, put elements in hash table
- key(target - element): value(index)
- check existence of current element in hash table, if present, return value and the current index as solution
- return empty solution
"""

def two_sum(array, target):
    """
    Time complexity : O(n). We traverse the list containing nn elements only once. Each look up in the table costs only O(1)O(1) time.

    Space complexity : O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.
    where n is the size of array
    """
    if not array or not isinstance(array, list) or not isinstance(target, int):
        return [] # throw exception is the right way
    table = {}
    for i in xrange(len(array)):
        if array[i] not in table:
            table[target-array[i]] = i
        else:
            return [table[array[i]], i]
    return []

if __name__ == '__main__':
    arr1 = [2, 7, 11, 15]
    print two_sum(arr1, 9)
