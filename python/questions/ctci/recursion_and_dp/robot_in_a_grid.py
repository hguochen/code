"""
CtCi
8.2 Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"
such that the robot cannot step on them. Design an algorithm to find a path for the robot from
the top left to the bottom right.
"""
class Coord(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
def robot_in_grid(grid):
    """
    Time: O(2^mn)
    Space: O(mn)
    where mn correspondes to the size of the grid

    with failed_coords memoization:
    Time: O(mn)
    Space: O(mn)
    """
    if not grid:
        return
    start = Coord(0, 0)
    end = Coord(len(grid)-1, len(grid[0])-1)
    result = []
    failed_coords = []
    if robot_in_grid_util(grid, start, end, result, failed_coords):
        return result
    return False

def robot_in_grid_util(grid, start, end, result, failed_coords):
    row, col = start.row, start.col
    # check start out of grid bounds
    if row >= len(grid) or col >= len(grid[0]):
        return False
    # check if start grid is restricted
    elif grid[row][col] == "X":
        failed_coords.append([row, col])
        return False
    elif [row, col] in failed_coords:
        return False
    if (row == end.row and col == end.col) or robot_in_grid_util(grid, Coord(row, col+1), end, result, failed_coords) or robot_in_grid_util(grid, Coord(row+1, col), end, result, failed_coords):
        result.insert(0, [row, col])
        return True
    # cache failed results
    failed_coords.append([row, col])
    return False

    

if __name__ == '__main__':
    grid = [[" " for _ in range(6)] for _ in range(7)]
    grid[0][3] = "X"
    grid[1][3] = "X"
    grid[2][3] = "X"
    grid[3][1] = "X"
    grid[4][4] = "X"
    grid[5][2] = "X"
    # for row in xrange(len(grid)):
    #     print grid[row]
    print robot_in_grid(grid)
