"""
http://www.spoj.com/problems/COINS/
"""

def max_usd(n):
    """
    Recursive solution
    max_usd(n) is the maximum number of USD that can be obtained with n value gold coin.

    Time: O(3^n) where n is the value given.
    Space: O(n)
    """
    if n <= 0:
        return 0
    elif n <= 11:
        return n
    return max_usd(n/2) + max_usd(n/3) + max_usd(n/4)

def max_usd_dp(n):
    """
    DP solution.
    Time: O(n)
    Space: O(n)
    """
    table = [0 for _ in range(n+1)]
    for i in xrange(12):
        table[i] = i
    return max_usd_dp_aux(n, table)

def max_usd_dp_aux(n, table):
    if n <= 0:
        return 0
    if table[n] != 0:
        return table[n]
    table[n] = max_usd_dp_aux(n/2, table) + max_usd_dp_aux(n/3, table) + max_usd_dp_aux(n/4, table)
    return table[n]

if __name__ == '__main__':
    print max_usd(12), max_usd_dp(12)
    print max_usd(16), max_usd_dp(16)