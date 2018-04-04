"""
CtCi
8.1 A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

let n be the number of steps to climb.
then triple_step(n) is the number of ways to run up the stairs

if n == 1:
    steps: 1
    ways: 1
if n == 2:
    steps: 11, 2
    ways: 2
if n == 3:
    steps: 111, 21, 12, 3
    ways: 4
...
so for n steps, the number of ways to climb the steps would be:
triple_step(n) = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

"""

def triple_step_recursion(n):
    """
    Time: O(3^n)
    Space: O(lgn)
    """
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    return triple_step_recursion(n-1) + triple_step_recursion(n-2) + triple_step_recursion(n-3)

def triple_step_dp(n):
    """
    Time: O(n)
    Space: O(lgn)
    """
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    memo = [-1 for _ in range(n+1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    result = triple_step_dp_util(n, memo)
    return result

def triple_step_dp_util(n, memo):
    if memo[n] != -1:
        return memo[n]
    memo[n] = triple_step_dp_util(n-1, memo) + triple_step_dp_util(n-2, memo) + triple_step_dp_util(n-3, memo)
    return memo[n]


if __name__ == '__main__':
    print triple_step_recursion(1), triple_step_dp(1) # 1
    print triple_step_recursion(2), triple_step_dp(2) # 2
    print triple_step_recursion(3), triple_step_dp(3) # 4
    print triple_step_recursion(4), triple_step_dp(4) # 4
    print triple_step_recursion(5), triple_step_dp(5) # 4
    print triple_step_recursion(6), triple_step_dp(6) # 4
    print triple_step_recursion(7), triple_step_dp(7) # 4
    print triple_step_recursion(8), triple_step_dp(8) # 4
