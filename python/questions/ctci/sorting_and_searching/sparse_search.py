"""
CtCi
10.5 Given a sorted array of strings that is interspersed with empty strings, write a method
to find the location of a given string.

BRUTE FORCE:
linearly search the element.
Time: O(n) Space: O(1)

better
Keep searching both sides of the arr if mid is empty string
if element found, search either side

"""

def sparse_search(arr, element):
    """
    Time avg: O(nlgn)
    Time worst: O(n)
    Space: O(1)
    """
    if not arr:
        return -1
    return binary_search(arr, element, 0, len(arr)-1)

def binary_search(arr, element, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == element:
        return mid
    if arr[mid] == "":
        res = binary_search(arr, element, low, mid-1) # search left
        if res == -1:
            res = binary_search(arr, element, mid+1, high) # search right
        return res
    elif element < arr[mid]:
        return binary_search(arr, element, low, mid-1)
    else:
        return binary_search(arr, element, mid+1, high)

def sparse_search2(arr, element):
    """
    Time avg: O(nlgn)
    Time worst: O(n)
    Space: O(1)
    """
    if not arr:
        return -1
    return binary_search2(arr, element, 0, len(arr)-1)

def binary_search2(arr, element, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == "":
        left = mid-1
        right = mid+1
        while True:
            if left < low and right > high:
                return -1
            elif left >= low and arr[left] != "":
                mid = left
                break
            elif right <= high and arr[right] != "":
                mid = right
                break
            left -= 1
            right += 1
    if arr[mid] == element:
        return mid
    elif element < arr[mid]:
        return binary_search2(arr, element, low, mid-1)
    return binary_search2(arr, element, mid+1, high)

if __name__ == '__main__':
    arr1 = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print sparse_search(arr1, "at") # 0
    print sparse_search(arr1, "ball") # 4
    print sparse_search(arr1, "car") # 7
    print sparse_search(arr1, "dad") # 10

    print sparse_search2(arr1, "at") # 0
    print sparse_search2(arr1, "ball") # 4
    print sparse_search2(arr1, "car") # 7
    print sparse_search2(arr1, "dad") # 10
