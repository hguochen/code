"""
https://www.geeksforgeeks.org/solve-dynamic-programming-problem/
This is a DP solving guide.

Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we can form
a number 'N' using the sum of the given three numbers.
Repetitions and different arrangements are allowed.

Total number of ways to form 6 is : 8
1+1+1+1+1+1
1+1+1+3
1+1+3+1
1+3+1+1
3+1+1+1
3+3
1+5
5+1

First of all, we decide the problem's state. 

We take a parameter n to decide state as it can uniquely identify any subproblem.

so, state(n) => number of arrangements to form n by using 1, 3, 5 as elements

Now we need to compute state(n).

With some intuition. We know that only the given elements can be used to form numbers.

Assume, we already have the solution for the following:
state(n=1)
state(n=2)
state(n=3)
state(n=4)
state(n=5)
state(n=6)

Now we want to calculate state(n=7). 

We do this by adding 1 to all possible combinations of state(n=6)
Eg : [ (1+1+1+1+1+1) + 1]
[ (1+1+1+3) + 1]
[ (1+1+3+1) + 1]
[ (1+3+1+1) + 1]
[ (3+1+1+1) + 1]
[ (3+3) + 1]
[ (1+5) + 1]
[ (5+1) + 1]

Then add 3 to all possible combinations of state(n=4)
Eg : [(1+1+1+1) + 3]
[(1+3) + 3]
[(3+1) + 3]

Then add 5 to all possible combinations of state(n=2)
Eg : [ (1+1) + 5]

Therefore, the result is:
state(7) = state(6) + state(4) + state(2)
OR
state(n) = state(n-1) + state(n-3) + state(n-5)
"""

def ways_to_n(n):
    """
    Recursive solution.
    Time: O(d^n) where d is the number of values available to use.
    Space: O(?)
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return ways_to_n(n-1) + ways_to_n(n-3) + ways_to_n(n-5) 

# Now that we have a recursive solution, we add memoization to the state to make it a DP solution
def ways_to_n_dp(n):
    table = [-1 for _ in range(n+1)]
    ways_to_n_dp_aux(n, table)

def ways_to_n_dp_aux(n, table):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    if table[n] != -1:
        return table[n]
    table[n] = ways_to_n_dp_aux(n-1, table) + ways_to_n_dp_aux(n-3, table) + ways_to_n_dp_aux(n-5, table)
    return table[n]