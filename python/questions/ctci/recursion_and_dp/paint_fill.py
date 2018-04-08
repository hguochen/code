"""
CtCi
8.10 Implement the paint fill function that one might see on many image editing programs.
This is, given a screen(represented by a two-dimensional array of colors), a point, and a new
color, fill in the surrounding area until the color changes from the original color.
"""

def paint_fill(screen, x, y, color):
    """
    Time: O(mn)
    Space: O(mn)
    where mn is the dimension of screen
    """
    if not screen:
        return
    visited = [[False for _ in range(len(screen[0]))] for _ in range(len(screen))]
    existing = screen[x][y]
    paint_fill_util(screen, visited, existing, x, y, color)
    return screen

def paint_fill_util(screen, visited, existing, x, y, color):
    if x < 0 or x >= len(screen) or y < 0 or y >= len(screen[0]) or screen[x][y] != existing or visited[x][y]:
        return
    visited[x][y] = True
    screen[x][y] = color

    # up
    paint_fill_util(screen, visited, existing, x-1, y, color)
    # right
    paint_fill_util(screen, visited, existing, x, y+1, color)
    # down
    paint_fill_util(screen, visited, existing, x+1, y, color)
    # left
    paint_fill_util(screen, visited, existing, x, y-1, color)

if __name__ == '__main__':
    screen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0]]

    for row in paint_fill(screen, 6, 7, 7):
        print row