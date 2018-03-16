"""
CLRS pg 391
Given 2 sequence strings X and Y, find the longest common subsequence of 2 sequences.
eg. 
seq1 = "ABCBDAB"
seq2 = "BDCABA"
answer = "BCBA"
We say, "BCA" is a longest common subsequence(LCS) of seq1 and seq2.
Another LCS is "BDAB"

"""
import copy

def brute_force(X, Y):
    """
    1. Generate all sequences of X.
    2. For each sequence of X check if it's a sequence of Y.
    3. return the longest sequence.

    Time: O(X+Y * 2^X)
    Space: O(1)

    Generating all sequences of X requires O(X * 2^X) time, thereafter comparing with string Y
    requires O(Y) time. Therefore O((X + Y) * 2^X)
    """
    if not X or not Y:
        return ""
    result = ""
    # loop over the binary string size numbers to generate each string
    size = '1' * len(X)

    for i in xrange(int(size, 2)+1):
        # get the binary masked representation for this number
        # eg. 5 => '101'
        mask = bin(i)[2:]
        mask = mask.rjust(len(X), '0')
        substring = ""
        for j in xrange(len(X)):
            if mask[j] == '1':
                substring += X[j]
        if is_subsequence(Y, substring) and len(substring) > len(result):
            result = substring
    return result

def is_subsequence(X, sub):
    """
    Return True if sub is a subsequence of X
    """
    if not X:
        return False
    if not sub:
        return True
    i, j = 0, 0

    while j < len(X):
        if X[j] == sub[i]:
            i += 1
        if i == len(sub):
            return True
        j += 1
    return False

def recursive(X, Y):
    """
    Time: O(2^XY)
    Space: O(1)
    """
    if not X or not Y:
        return ""
    i = len(X) - 1
    j = len(Y) - 1
    result = [0, ""]
    lcs_length = recursive_aux(X, Y, i, j, result)
    return result


def recursive_aux(X, Y, i, j, result):
    """
    With direct reference to the recursive formula.
    if X[i] == Y[j]:
        LCS((X[i-1], Y[j-1]))
    if X[i] != Y[j]:
        max(LCS(X[i-1], Y[j]), LCS(X[i], Y[j-1]))
    """
    if i == -1 or j == -1:
        return result
    if X[i] == Y[j]:
        if X[i] not in result[1]:
            result[0] += 1
            result[1] += X[i]
        return recursive_aux(X, Y, i-1, j-1, result)
    # X[i] != Y[j]
    return max(recursive_aux(X, Y, i-1, j, result), recursive_aux(X, Y, i, j-1, result))

def dynamic_programming(X, Y):
    """
    Time: O(XY)
    Space: O(XY)
    """
    # X is col, Y is row
    table = [[0 for _ in range(len(X))] for _ in range(len(Y))]
    pointer = [[[-1, -1] for _ in range(len(X))] for _ in range(len(Y))]

    if X[0] == Y[0]:
        table[0][0] == 1
    # init col 0 values
    for row in range(1, len(table)):
        if X[0] == Y[row]:
            table[row][0] = 1
        else:
            table[row][0] = table[row-1][0]
    # init row 0 values
    for col in range(1, len(table[0])):
        if X[col] == Y[0]:
            table[0][col] = 1
        else:
            table[0][col] = table[0][col-1]
    # populate table based on recursive formula
    for row in xrange(1, len(table)):
        for col in xrange(1, len(table[row])):
            if X[col] == Y[row]:
                table[row][col] = table[row-1][col-1] + 1
                pointer[row][col] = [row-1, col-1]
            elif table[row-1][col] < table[row][col-1]:
                table[row][col] = table[row][col-1]
                pointer[row][col] = [row, col-1]
            else:
                table[row][col] = table[row-1][col]
                pointer[row][col] = [row-1, col]
    for x in xrange(len(table)):
        print table[x]
    for x in xrange(len(pointer)):
        print pointer[x]
    return table[len(Y)-1][len(X)-1]

if __name__ == '__main__':
    X1 = "ABCBDAB"
    Y1 = "BDCABA"

    X2 = "AGGTAB"
    Y2 = "GXTXAYB"

    X3 = "BDCABA"
    Y3 = "ABCBDAB"
    print brute_force(X1, Y1), recursive(X1, Y1), dynamic_programming(X1, Y1)
    print brute_force(X2, Y2), recursive(X2, Y2), dynamic_programming(X2, Y2)
    print brute_force(X3, Y3), recursive(X3, Y3), dynamic_programming(X3, Y3)
