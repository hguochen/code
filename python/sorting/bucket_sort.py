"""
Bucket Sort

We can use bucket sort assuming we know the upper and lower bound of all the element values.

Time:
worst - O(n^2) where n is the number of elements in array
average - O(n + k) where k is the number of buckets
Space: O(n)
"""

def bucket_sort(array):
    buckets = [[] for _ in range(10)]
    for value in array:
        index = value // 10
        buckets[index].append(value)
        if len(buckets[index]) > 1:
            for i in xrange(len(buckets[index])-2, -1, -1):
                if buckets[index][i] > buckets[index][i+1]:
                    buckets[index][i], buckets[index][i+1] = buckets[index][i+1], buckets[index][i]
                else:
                    break
    # for sublist in buckets:
    #   for item in sublist:
    #       array.append(item)
    array = [value for sublist in buckets for value in sublist]
    return array
            
        

if __name__ == '__main__':
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    arr4 = [1, 4, 1, 2, 7, 5, 2]
    print bucket_sort(arr1)
    print bucket_sort(arr2)
    print bucket_sort(arr3)
    print bucket_sort(arr4)