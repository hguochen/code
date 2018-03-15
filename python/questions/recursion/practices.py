# https://www.geeksforgeeks.org/practice-questions-for-recursion/
# https://www.geeksforgeeks.org/practice-questions-for-recursion-set-2/

def fun1(x, y):
    """
    Function computs the equation ((1+2+3+... +x) + y)
    and returns the results
    Eg. fun1(3,5) => 1+2+3 + 5 = 11
    """
    if x == 0:
        return y
    return fun1(x-1, x + y)

def fun2(arr, start, end):
    """
    Recursive implementation of selection sort
    """
    if start >= end:
        return
    index = min_index(arr, start, end)

    temp = arr[start]
    arr[start] = arr[index]
    arr[index] = temp
    fun2(arr, start+1, end_index)

def fun3(n):
    """
    The function calculates and return log2(n).
    eg. 
    if n is between 8 and 15 then func1 returns 3.
    if n is between 16 to 31 then fun1 returns 4.
    """
    if n == 1:
        return 0
    return 1 + fun3(n/2)

def fun4(n):
    """
    Prints the binary equivalent of n.
    Print starts from the most significant bit
    eg.
    if n = 21, then fun4(21) = 10101
    """
    if n == 0:
        return
    fun4(n/2)
    print n % 2

def fun5(n):
    """
    Prints the arithmetic progression of stars from 1 to n
    fun5(3) =>
    *
    * *
    * * *
    """
    if n > 1:
        fun5(n-1)
    for i in xrange(n):
        print " * "

def fun6(n):
    """
    Prints the 2 * values of n in increasing order up to 1000,
    then prints the values in reverse order.
    """
    if n <= 0:
        return
    if n > 1000:
        return
    print n
    fun6(2*n)
    print n

def fun7(n):
    """
    Output: 0 1 2 0 3 0 1
    """
    if x > 0:
        x -= 1
        fun7(x)
        print x
        x -= 1
        fun7(x)

def fun8(arr, n):
    """
    Return the biggest value in the array.
    """
    if n == 1:
        return arr[0]
    x = fun8(arr, n-1)
    if x > a[n-1]:
        return x
    return a[n-1]

def fun9(a, b):
    """
    calculates a * b
    """
    if b == 0:
        return 0
    if b % 2 == 0: # even b
        return fun9(a + a, b / 2) # a double, b half
    return fun9(a + a, b/2) + a

def fun10(a, b):
    """
    calculates a^b
    """
    if b == 0:
        return 1
    if b % 2 == 0:
        return fun10(a*a, b/2)
    return fun10(a*a, b/2) * a

def fun11(count):
    """
    """
    print count
    if count < 3:
        count += 1
        fun11(fun11(fun11(count)))
    return count

def fun12(n):
    if n <= 1:
        return 1
    return fun12(n-1) + fun12(n-2)



if __name__ == '__main__':
    fun4(6)
    print fun12(5)