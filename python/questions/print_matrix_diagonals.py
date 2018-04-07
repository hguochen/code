"""
Given an MxN matrix, write code which prints out the diagonals (from upper right to lower left) of the matrix.
In this example where M = 4, N = 3:
[[9, 3, 2],
 [8, 6, 1],
 [5, 5, 6],
 [1, 2, 8]]

(i, j), (i, j+1)
(i+1, j)

Your code should print out:
9
3 8
2 6 5
1 5 1
6 2
8
"""

def print_matrix(matrix):
    """
    Time: O(mn)
    Space: O(mn)
    
    """
    
    if len(matrix) < 1:
        return
    truth = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    temp = []
    queue = [[0, [0, 0]]]
    
    while len(queue) > 0:
        cell = queue.pop(0)
        layer, row, col = cell[0], cell[1][0], cell[1][1]
        if len(temp) < 1:
            temp.append(cell)
        else:
            last_value = temp[-1]
            if last_value[0] == layer:
                temp.append(cell)
            else:
                # print and flush temp
                for item in temp:
                    value = matrix[item[1][0]][item[1][1]]
                    print value,
                print
                temp = [cell]
        truth[row][col] = True
        # queue up right
        if col+1 < len(matrix[0]) and not truth[row][col+1] and not [layer+1, [row, col+1]] in queue:
            queue.append([layer+1, [row, col+1]])
        # queue up down
        if row+1 < len(matrix) and not truth[row+1][col] and not [layer+1, [row+1, col]] in queue:
            queue.append([layer+1, [row+1, col]])
    if len(temp) < 1:
        return
    for item in temp:
        value = matrix[item[1][0]][item[1][1]]
        print value,
    print
    return
                
    
    
def print_temp(matrix):
    for row in range(len(matrix)):
        print matrix[row]

matrix1 = [[9, 3, 2], [8, 6, 1], [5, 5, 6], [1, 2, 8]]

print_matrix(matrix1)
