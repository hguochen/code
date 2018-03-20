"""
https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

"""
import sys

def min_cost_path(matrix, start, end):
    if matrix is None:
        return
    return min_cost_path_aux(matrix, start, end)

def min_cost_path_aux(matrix, start, end):
    """
    Time: O(3^n) where n is the size of the matrix
    Space: O(n)
    """
    if start == end:
        return matrix[start[0]][start[1]]
    if end[0] < 0 or end[0] >= len(matrix) or end[1] < 0 or end[1] >= len(matrix[0]):
        # lies outside of matrix
        return sys.maxint
    return matrix[end[0]][end[1]] + min(min_cost_path_aux(matrix, start, [end[0]-1, end[1]-1]),
        min_cost_path_aux(matrix, start, [end[0]-1, end[1]]),
        min_cost_path_aux(matrix, start, [end[0], end[1]-1]))

def min_cost_path_dp(matrix, start, end):
    """
    Time: O(nm) where n is matrix row, m is matrix length
    Space: O(nm)
    """
    table = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    table[0][0] = matrix[0][0]

    # init for first column
    for i in range(1, len(table)):
        table[i][0] = table[i-1][0] + matrix[i][0]
    # init for first row
    for i in range(1, len(table[0])):
        table[0][i] = table[0][i-1] + matrix[0][i]

    for i in range(1, len(table)):
        for j in range(1, len(table[i])):
            table[i][j] = min(table[i-1][j-1], table[i-1][j], table[i][j-1]) + matrix[i][j]
    return table[end[0]][end[1]]

if __name__ == '__main__':
    matrix1 = [
        [1,2,3],
        [4,8,2],
        [1,5,3]
    ]
    print min_cost_path(matrix1, [0, 0], [2, 2])
    print min_cost_path_dp(matrix1, (0, 0), (2, 2))