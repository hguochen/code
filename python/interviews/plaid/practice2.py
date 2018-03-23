

# print content # list
import re

def draw_ascii(content):
    """
    assume 110 by 100 grid.

    Time: O(n) 
    Space: O(1)
    where n is the size of the content
    """

    matrix = [[" " for _ in range(100)] for _ in range(100)]
    if len(content) < 1:
        return matrix
    pattern = r'\[([0-9]{1,2}),([0-9]{1,2}),([0-9]{1,2})\]'
    for item in content:
        match_obj = re.match(pattern, item, re.I)
        x = int(match_obj.group(1))
        y = int(match_obj.group(2))
        value = int(match_obj.group(3))
        
        matrix[y][x] = chr(value)
    return matrix

if __name__ == '__main__':
    with open('data.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content] 

    result = draw_ascii(content)
    for row in range(len(result)):
        for col in range(len(result[row])):
            print result[row][col],
        print ""
