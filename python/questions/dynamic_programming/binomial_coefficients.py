"""
Compute the nth binomial coefficients.

1: 1
2: 1 1
3: 1 2 1
4: 1 3 3 1
5: 1 4 6 4 1
6: 1 5 10 5 1
"""

def binomial_coefficients(n):
    """
    Time: O(n^2)
    Space: O(n^2)
    """
    if n <= 0:
        return 0
    table = [[0 for _ in range(n)] for _ in range(n+1)]
    for i in xrange(1, len(table)):
        table[i][0] = 1

    for i in xrange(2, len(table)):
        for j in xrange(1,len(table[i])):
            table[i][j] = table[i-1][j-1] + table[i-1][j]

    return table[n]


if __name__ == '__main__':
    print binomial_coefficients(6)