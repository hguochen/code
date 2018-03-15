# Fibonacci numbers module

def fib(n):
    """
    Write Fibonacci series up to n
    """
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def fib_3(n):
    """
    Compute the nth fibonacci number with recursion.

    Time: O(2^n)
    Space: O(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_3(n-1) + fib_3(n-2)

def fib_4(n):
    memo = [0 for _ in range(n+1)]
    return fibonacci_with_memoization(n, memo)

def fibonacci_with_memoization(n, memo):
    """
    Time: O(n)
    Space: O(n)
    """
    if n == 0 or n == 1:
        return n
    if memo[n] == 0:
        memo[n] = fibonacci_with_memoization(n-1, memo) + fibonacci_with_memoization(n-2, memo)
    return memo[n]

def fibonacci_bottom_up_memoization(n):
    """
    Compute nth fibonacci number with bottom up DP approach
    Time: O(n)
    Space: O(n)
    """
    if n == 0 or n == 1:
        return n
    memo = [0 for _ in range(n+1)]
    memo[1] = 1
    for i in xrange(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]

def fibonacci_optimized(n):
    """
    Getting rid of memo table.

    Time: O(n)
    Space: O(1)
    """
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in xrange(2, n):
        c = a + b
        a = b
        b = c
    return a + b

if __name__ == '__main__':

    print fib_3(6)
    print fib_4(6)
    print fibonacci_bottom_up_memoization(1)
    print fibonacci_bottom_up_memoization(2)
    print fibonacci_bottom_up_memoization(3)
    print fibonacci_bottom_up_memoization(4)
    print fibonacci_bottom_up_memoization(5)
    print fibonacci_bottom_up_memoization(6)
    print fibonacci_bottom_up_memoization(7)
