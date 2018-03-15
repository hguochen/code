"""
CLRS pg 360

Given a rod of n inches and a table of prices for i = 1,2,...,n.
Determine the maximum revenue obtainable by cutting up the rod
and selling the pieces. Note that if the price for a rod of
length n is large enough, an optimal solution may require no cutting
at all.

length | price
1 | 1
2 | 5
3 | 8
4 | 9
5 | 10
6 | 17
7 | 17
8 | 20
9 | 24
10| 30
"""
import sys

def cut_rod(price, n):
    """
    Recursive top down implementation
    Time: O(2^n)
    """
    if n == 0:
        return 0
    result = -sys.maxint - 1 # minimum integer value
    for i in xrange(1,n+1):
        result = max(result, price[i] + cut_rod(price, n-i))
    return result

def cut_rod_memo(price, n):
    """
    Top down memoized cut rod.

    Time: O(n^2)
    Space: O(n)
    """

    memo = [-sys.maxint-1 for _ in range(n+1)]
    return cut_rod_memo_aux(price, n, memo)

def cut_rod_memo_aux(price, n, memo):
    # value has already been computed, just return
    if memo[n] >= 0:
        return memo[n]
    # if n is 0
    result = 0
    # compute the value at which n is not 0
    if n != 0:
        result = -sys.maxint - 1
        for i in xrange(1,n+1):
            result = max(result, price[i] + cut_rod_memo_aux(price, n - i, memo))
    memo[n] = result
    return memo[n]

def cut_rod_bottom_up(price, n):
    """
    Bottom up memoization.

    Time: O(n^2)
    Space: O(n)
    """
    memo = [-sys.maxint-1 for _ in range(n+1)]
    # holds the optimal size of the first piece to cut off
    solution = [-sys.maxint-1 for _ in range(n+1)]
    solution[0] = 0
    memo[0] = 0

    for i in range(1, n+1):
        result = -sys.maxint-1
        for j in xrange(1,i+1):
            if result < price[j] + memo[i-j]:
                result = price[j] + memo[i-j]
                # store the first piece length to cut here
                solution[i] = j
        memo[i] = result
    return memo[n], solution

def print_cut_rod(price, n):
    memo, solution = cut_rod_bottom_up(price, n)
    while n > 0:
        print solution[n],
        n = n - solution[n]
    print ""
    return

if __name__ == '__main__':
    prices = {
        1: 1,
        2: 5,
        3: 8,
        4: 9,
        5: 10,
        6: 17,
        7: 17,
        8: 20,
        9: 24,
        10: 30
    }
    print cut_rod(prices, 1), cut_rod_memo(prices, 1), cut_rod_bottom_up(prices, 1)
    print cut_rod(prices, 2), cut_rod_memo(prices, 2), cut_rod_bottom_up(prices, 2)
    print cut_rod(prices, 3), cut_rod_memo(prices, 3), cut_rod_bottom_up(prices, 3)
    print cut_rod(prices, 4), cut_rod_memo(prices, 4), cut_rod_bottom_up(prices, 4)
    print cut_rod(prices, 5), cut_rod_memo(prices, 5), cut_rod_bottom_up(prices, 5)
    print cut_rod(prices, 6), cut_rod_memo(prices, 6), cut_rod_bottom_up(prices, 6)
    print cut_rod(prices, 7), cut_rod_memo(prices, 7), cut_rod_bottom_up(prices, 7)
    print cut_rod(prices, 8), cut_rod_memo(prices, 8), cut_rod_bottom_up(prices, 8)
    print cut_rod(prices, 9), cut_rod_memo(prices, 9), cut_rod_bottom_up(prices, 9)
    print cut_rod(prices, 10), cut_rod_memo(prices, 10), cut_rod_bottom_up(prices, 10)

    print_cut_rod(prices, 1)
    print_cut_rod(prices, 2)
    print_cut_rod(prices, 3)
    print_cut_rod(prices, 4)
    print_cut_rod(prices, 5)
    print_cut_rod(prices, 6)
    print_cut_rod(prices, 7)
    print_cut_rod(prices, 8)
    print_cut_rod(prices, 9)
    print_cut_rod(prices, 10)
