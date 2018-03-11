"""
Merge Sort

Time: O(nlgn)
Space: O(n) 
"""

def merge_sort(array, low, high):
    if high > low:
        mid = (low + high) / 2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)
    return array

def merge(array, low, mid, high):
    temp = array[:]
    left_index = low
    right_index = mid + 1
    index = low

    while left_index <= mid and right_index <= high:
        if temp[left_index] < temp[right_index]:
            array[index] = temp[left_index]
            left_index += 1
        else:
            array[index] = temp[right_index]
            right_index += 1
        index += 1

    while left_index <= mid:
        array[index] = temp[left_index]
        left_index += 1
        index += 1
    while right_index <= high:
        array[index] = temp[right_index]
        right_index += 1
        index += 1
    return

if __name__ == "__main__":
    arr1 = [4,3,2,10,12,1,5,6]
    arr2 = [64, 25, 12, 22, 11]
    arr3 = [38, 27, 43, 3, 9, 82, 10]
    print merge_sort(arr1, 0, len(arr1)-1)
    print merge_sort(arr2, 0, len(arr2)-1)
    print merge_sort(arr3, 0, len(arr3)-1)
