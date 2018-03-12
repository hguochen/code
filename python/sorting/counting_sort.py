"""
Counting sort.
https://www.geeksforgeeks.org/counting-sort/

Time: O(n + k) where n is the number of elements in array
Space: O(k) where k is the max_range
"""

def counting_sort(array, range_max):
    counts = [0 for _ in range(range_max+1)]
    # construct histogram of the frequency of each element
    for value in array:
        counts[value] += 1
    
    # construct aggregated histogram of each element
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    result = [None] * len(array)
    
    for value in array:
        index = counts[value] - 1
        result[index] = value
        counts[value] -= 1
    return result

if __name__ == '__main__':
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    arr4 = [1, 4, 1, 2, 7, 5, 2]
    print counting_sort(arr1, 20)
    print counting_sort(arr2, 70)
    print counting_sort(arr3, 90)
    print counting_sort(arr4, 10)
