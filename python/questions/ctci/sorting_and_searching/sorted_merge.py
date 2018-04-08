"""
CtCi
10.1 You are given two sorted arrays, A and B, where A has a larger enough buffer at the 
end to hold B. Write a method to merge B into A in sorted order.
"""

def sorted_merge(A, B):
    """
    Time: O(n)
    Space: O(1)
    where n is the size of the longer sorted array among A and B.
    """
    if not B:
        return A
    elif not A:
        return B
    largest_A_index = -1
    for i in xrange(len(A)):
        if A[i] is None:
            largest_A_index = i-1
            break
    largest_B_index = len(B) - 1

    j = len(A) - 1
    while largest_B_index >= 0:
        if A[largest_A_index] > B[largest_B_index]:
            A[j] = A[largest_A_index]
            largest_A_index -= 1
        else:
            A[j] = B[largest_B_index]
            largest_B_index -= 1
        j -= 1
    return A


if __name__ == '__main__':
    A = [1,2,3,4,5,6,10,45, None, None, None, None, None]
    B = [11, 12, 22, 25, 64]
    
    print sorted_merge(A, B)
