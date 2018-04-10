"""
CtCi
10.9 Given an M x N matrix in which each row and each column is sorted in ascending order,
write a method to find an element.

BRUTE FORCE:
Time: O(mn)
Space: O(1)

BETTER:
Time: O(m+n)
Space: O(1)

"""

def search(matrix, val):
    """
    Start from the top right.
    if cell == val, return the cell
    if val < cell, move 1 cell left
    if val > cell, move 1 cell down

    Time: O(m+n)
    Space: O(1)
    """
    if not matrix:
        return None
    i, j = 0, len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if matrix[i][j] == val:
            return (i, j)
        if val < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return None

if __name__ == '__main__':
    matrix1 = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]
    print search(matrix1, 10) # (0, 0)
    print search(matrix1, 20) # (0, 1)
    print search(matrix1, 30) # (0, 2)
    print search(matrix1, 40) # (0, 3)
    print search(matrix1, 15) # (1, 0)
    print search(matrix1, 25) # (1, 1)
    print search(matrix1, 35) # (1, 2)
    print search(matrix1, 45) # (1, 3)
    print search(matrix1, 27) # (2, 0)
    print search(matrix1, 29) # (2, 1)
    print search(matrix1, 37) # (2, 2)
    print search(matrix1, 48) # (2, 3)
    print search(matrix1, 32) # (3, 0)
    print search(matrix1, 33) # (3, 1)
    print search(matrix1, 39) # (3, 2)
    print search(matrix1, 50) # (3, 3)