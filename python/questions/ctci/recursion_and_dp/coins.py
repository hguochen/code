"""
CtCi
8.12 Given an infinite number of quarters(25), dimes(10), nickels(5) and pennies(1), write
code to calculate the number of ways of representing n cents.
"""
def ways(n, coins):
    """
    Time: O(mn)
    Space: O(mn)
    where m is number of coin denominations, n is size of n input
    """
    if n < 1:
        return 1
    if not coins:
        return 0
    table = [[-1 for _ in range(n+1)] for _ in range(len(coins))]
    for i in xrange(n+1):
        table[0][i] = 1

    for row in xrange(1, len(table)):
        for col in xrange(0, len(table[row])):
            if col < coins[row]:
                table[row][col] = table[row-1][col]
            else:
                table[row][col] = table[row][col-coins[row]] + table[row-1][col]
    for row in table:
        print row
    return table[len(coins)-1][n]

if __name__ == '__main__':
    coins = [1,5,10,25]
    print ways(15, coins)
