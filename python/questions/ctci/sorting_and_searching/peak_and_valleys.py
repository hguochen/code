"""
CtCi
10.11 In an array of integers, a "peak" is an element which is greater than or equal to
the adjacent integers and a "valley" is an element which is less than or equal to the
adjacent integers. For example, [5,8,6,2,3,4,6], [8,6] are peaks and [5,2] are valleys.
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

"""

def peak_and_valley(arr):
    """
    Time: O(nlgn) from sorting
    Space: O(1)
    """
    if not arr or len(arr) < 3:
        return arr
    arr = sorted(arr)
    for i in xrange(2, len(arr), 2):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

def peak_and_valley2(arr):
    """
    Time: O(n)
    Space: O(1)
    """
    if not arr or len(arr) < 3:
        return arr
    for i in xrange(1,len(arr), 2):
        # biggest = arr[i]
        # big_idx = i
        # if arr[i-1] > biggest:
        #     biggest = arr[i-1]
        #     big_idx = i-1
        # if i+1 < len(arr) and arr[i+1] > biggest:
        #     biggest = arr[i+1]
        #     big_idx = i+1
        # if big_idx != i:
        #     arr[i], arr[big_idx] = arr[big_idx], arr[i]
        if i+1 < len(arr):
            biggest = max(arr[i], arr[i-1], arr[i+1])
        else:
            biggest = max(arr[i], arr[i-1])
        if i+1 < len(arr) and biggest == arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        elif biggest == arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    return arr

if __name__ == '__main__':
    arr1 = [5,3,1,2,3]
    print peak_and_valley(arr1)
    print peak_and_valley2(arr1)