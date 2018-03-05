# Given an unsorted array that may contain duplicates.Alsogiven a number k which
# is smaller than size of array. Write a function that returns true if array
# contains duplicates within k distance.

def brute(array, k):
    """
    Time: O(kn) where n is the size of array. and k is the value k
    Space: O(1)
    Note: the inner loop always runs a max of k - 1 times, so it's considered a constant here.
    """
    # check for boundary cases
    # loop through array
    #   set the end checking index as i + k index
    #   if i + k index is out of bounds return false
    #   inner loop to check each index for same value as index i until hits i + k index
    #       if same, return true
    # outside loop return false
    if not array or not isinstance(k, (int, long)):
        print "array is empty or k is not an integer"
        return
    for i in range(len(array)-1):
        for j in range(i + 1, i+k+1):
            if j >= len(array):
                break
            elif array[i] == array[j]:
                return True
    return False


def has_duplicate_element(array, k):
    """
    Time: O(n)
    Space: O(n)
    """
    # put all elements in array into a hash table with key = element, value = index
    # loop through the table, if there are more than 1 index in a key, check if they are within k space
    if not array or not isinstance(k, (int, long)):
        print "array is empty or k is not an integer"
        return
    table = {}
    for i in range(len(array)):
        if array[i] not in table:
            table[array[i]] = [i]
        elif i - table[array[i]][-1] <= k:
            return True
        else:
            table[array[i]].append(i)
    return False

if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 1, 2, 3, 4]
    k1 = 3
    print brute(arr1, 3)
    print has_duplicate_element(arr1, 3)

    arr2 = [1,2,3,1,4,5]
    k2 = 3
    print brute(arr2, 3)
    print has_duplicate_element(arr2, 3)

    arr3 = [1,2,3,4,5]
    k3 = 3
    print brute(arr3, 3)
    print has_duplicate_element(arr3, 3)

    arr4 = [1,2,3,4,4]
    k4 = 3
    print brute(arr4, 3)
    print has_duplicate_element(arr4, 3)
