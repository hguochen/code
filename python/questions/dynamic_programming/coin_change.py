"""
https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

state
Let n be the change value
so, ways(Set, n) will be the number of ways using the set to compute value n
"""
 
 def ways_recursive(S, m, n)
    """
    Time: O(2^m) where m is the size of the set S
    Space:O(m)
    Note: in some programming language where optimization is done on tail recursion,
    the space can be P(1)
    """
    
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1
 
    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;
 
    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0
 
    # count is sum of solutions (i) 
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );

def ways_dp(values, change):
    """
    Assume values are given in non-decreasing order
    Time: O(nm) where n is the number of values, m is change value
    Space: O(nm)
    """
    if len(values) == 0:
        return 0
    elif change == 0:
        return 1
    table = [[None for _ in range(change+1)] for _ in range(len(values))]
    # there's 1 way to give a change of 0
    for i in xrange(len(table)):
        table[i][0] = 1
    # init the ways to change with the smallest denomination
    for i in xrange(1, len(table[0])):
        if i % values[0] == 0:
            table[0][i] = 1
        else:
            table[0][i] = 0
    for row in xrange(1,len(table)):
        for col in xrange(1,len(table[row])):
            if col < values[row]:
                table[row][col] = table[row-1][col]
            else:
                table[row][col] = table[row-1][col] + table[row][col-values[row]]
    for i in xrange(len(table)):
        print table[i]
    return table[-1][-1]

if __name__ == '__main__':
    N1 = 4
    S1 = (1,2,3)

    N2 = 10
    S2 = (2, 5, 3, 6)

    print ways_dp(S1, N1)
    print ways_dp(S2, N2)