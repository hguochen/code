"""
Given two strings str1 and str2 and below operations that can be performed on str1.
1. insert
2. remove
3. replace
Find minimum number of edits required to convert str1 into str2.
"""

def string_compare(str1, str2, i, j):
    """
    Return the minimum number of edits required to convert str1 into str2
    Time: O(3^(X+Y)) where X is len of str1, Y is len of str2
    Space: O(1)
    """
    opt = {
        "MATCH": 0,
        "INSERT": 0,
        "DELETE": 0
    }
    if i == 0:
        return j
    elif j == 0:
        return i

    opt["MATCH"] = string_compare(str1, str2, i-1, j-1) + match(str1[i], str2[j])
    opt["INSERT"] = string_compare(str1, str2, i, j-1) + 1
    opt["DELETE"] = string_compare(str1, str2, i-1, j) + 1
    
    lowest_cost = opt["MATCH"]
    for key, value in opt.iteritems():
        if value < lowest_cost:
            lowest_cost = value
    return lowest_cost

class Cell(object):
    def __init__(self, cost=0, op=None):
        super(Cell, self).__init__()
        self.cost = cost
        self.op = op
        
def string_compare_dp(str1, str2):
    """
    DP solution
    Return the minimum number of edits required to convert str1 into str2
    Time: O(mn) where m is size of str1, n is size of str2
    Space: O(mn)
    """
    # str1 correspondes to column
    # str2 correspondes to row
    table = [[Cell() for _ in range(len(str1))] for _ in range(len(str2))]
    # determines whether the first character is the same or not
    if str1[0] == str2[0]:
        table[0][0].cost = 0
    else:
        table[0][0].cost = 1

    # if current i and j character matches, no new costs are incurred, we take the previous i-1, j-1 value
    # if current i and j character does not match, we take the minimum costs of the 3 operations and add this operation.
    for row in xrange(len(table)):
        for col in xrange(len(table[row])):
            if row == 0 and col == 0:
                continue
            if row == 0:
                table[0][col].cost = table[0][col-1].cost + 1
            elif col == 0:
                table[row][0].cost = table[row-1][0].cost + 1
            else:
                if str1[col] == str2[row]:
                    table[row][col].cost = table[row-1][col-1].cost
                    table[row][col].op = "MATCH"
                else:
                    min_value = table[row-1][col-1].cost
                    op = "SUBSTITUTE"
                    if table[row-1][col].cost < min_value:
                        min_value = table[row-1][col].cost
                        op = "DELETE"
                    if table[row][col-1].cost < min_value:
                        min_value = table[row][col-1].cost
                        op = "INSERT"
                    table[row][col].cost = 1 + min_value
                    table[row][col].op = op

    for row in xrange(len(table)):
        for col in xrange(len(table[row])):
            print table[row][col].cost,
        print ""
    return table[len(str2)-1][len(str1)-1].cost

def match(char1, char2):
    if char1 == char2:
        return 0
    return 1

if __name__ == '__main__':
    str1 = "shot"
    str2 = "spot"

    str3 = "you should not"
    str4 = "thou shalt not"

    str5 = "sunday"
    str6 = "saturday"
    print string_compare(str1, str2, len(str1)-1, len(str2)-1)
    print string_compare_dp(str1, str2)

    print string_compare_dp(str3, str4)
    print string_compare_dp(str5, str6)