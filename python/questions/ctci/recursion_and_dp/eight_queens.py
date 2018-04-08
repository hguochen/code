"""
CtCi
8.12 Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means
all diagonals, not just the two that bisect the board.
"""
import copy

GRID_SIZE = 8

def place_queens(row, columns, results):
    """
    Time: O(2^n)
    Space: O(m)
    where n is the size of the grid. m is the number of solutions generated.
    """
    if row == GRID_SIZE:
        results.append(copy.deepcopy(columns))
        return
    for col in xrange(GRID_SIZE):
        if is_valid(columns, row, col):
            columns[row] = col # place queen
            place_queens(row+1, columns, results)

def is_valid(columns, row1, col1):
    for row2 in xrange(0,row1):
        col2 = columns[row2]
        # check if row1, col1, invalidates row2 col2 as a queen spot
        if col1 == col2:
            return False

        # check diagonals, if distance between the column equals the dist betwen the rows
        # then they are in the same diagonal
        col_dist = abs(col2 - col1)
        # row1 > row2 so no need for abs
        row_dist = row1 - row2
        if col_dist == row_dist:
            return False
    return True

if __name__ == '__main__':
    columns = [-1 for _ in range(GRID_SIZE)]
    results = []
    place_queens(0, columns, results)
    for row in results:
        print row
