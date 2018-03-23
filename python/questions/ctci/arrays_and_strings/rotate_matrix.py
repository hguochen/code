"""
CtCi
1.7 Given an image representated by an NxN matrix, where each pixel in the
image is 4 bytes, write a method to roate the image by 90 degrees. Can you do this in place?
"""
import unittest

def rotate_matrix_right(matrix):
    """
    Time: O(n^2)
    Space: O(1)
    where n is the length of matrix
    """
    if len(matrix) < 1 or len(matrix) != len(matrix[0]):
        return False

    for layer in xrange(len(matrix)/2):
        first = layer
        last = len(matrix) - 1 - layer
        for i in xrange(first, last):
            offset = i - first
            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # btm -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            # right -> btm
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
        # for i in range(len(matrix)):
        #     print matrix[i]
    return matrix

class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix_right(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
    # test = [
    #     [1, 2, 3, 4, 5],
    #     [6, 7, 8, 9, 10],
    #     [11, 12, 13, 14, 15],
    #     [16, 17, 18, 19, 20],
    #     [21, 22, 23, 24, 25]
    # ]
    # for row in rotate_matrix_right(test):
    #     print row
