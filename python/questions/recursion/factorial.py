"""
Return the factorial of the given number
"""

def factorial(n):
    # base case
    if n == 1:
        return 1
    return n * factorial(n - 1)

def print_fun(test):
    if test < 1:
        return
    print test, " "
    print_fun(test-1)
    print test, " "
    return

if __name__ == "__main__":
    print factorial(5)
    print_fun(5)