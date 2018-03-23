"""
CtCi
1.8 Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.

- traverse every cell
- whenever u see a zero, mark every other row, col, non zero value as -1. leave 0 or -1 as is.
- traverse every cell again, change every -1 to 0
"""
import unittest

def zero_matrix(matrix):
    """
    Time: O(nm)
    Space: O(1)
    where n is matrix row, m is matrix column
    """
    if not matrix:
        return
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[row])):
            if matrix[row][col] == 0:
                matrix = mark_row_col(matrix, row, col)

    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[row])):
            if matrix[row][col] == -1:
                matrix[row][col] = 0
    return matrix

def mark_row_col(matrix, row, col):
    for i in xrange(len(matrix)):
        if matrix[i][col] != 0:
            matrix[i][col] = -1
    for j in xrange(len(matrix[row])):
        if matrix[row][j] != 0:
            matrix[row][j] = -1
    return matrix


class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)
        
if __name__ == "__main__":
    unittest.main()
