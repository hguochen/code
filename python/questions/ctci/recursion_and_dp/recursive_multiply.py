"""
CtCi
8.5 Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should minimize
the number of those operations.
"""

def multiply_by_addition(a, b):
    sign = "+"
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = "-"
    result = 0
    for i in xrange(abs(b)):
        result += abs(a)
    if sign == "-":
        result = 0 - result
    return result

def multiply_by_addition_recursive(a, b):
    return multiply_by_addition_recursive_util(a, b, 0, 0)

def multiply_by_addition_recursive_util(a, b, i, result):
    if i >= abs(b):
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            return 0 - result
        return result
    result += a
    return multiply_by_addition_recursive_util(a, b, i+1, result)

def min_product(a, b):
    """
    Time: O(lgs)
    Space: O(1)
    where s is the value of smaller integer
    """
    is_positive = True
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        is_positive = False
    bigger = b if a < b else a # a < b? b : a
    smaller = a if a < b else b # a < b? a : b
    result = min_product_util(abs(smaller), abs(bigger))
    if is_positive:
        return result
    return 0 - result

def min_product_util(smaller, bigger):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1 # divide by 2
    half_prod = min_product_util(s, bigger)

    if smaller % 2 == 0:
        return half_prod + half_prod
    return half_prod + half_prod + bigger

if __name__ == '__main__':
    print multiply_by_addition(3, 5), multiply_by_addition_recursive(3, 5)
    print multiply_by_addition(6, 8), multiply_by_addition_recursive(6, 8)
    print multiply_by_addition(-6, 8), multiply_by_addition_recursive(-6, 8)
    print multiply_by_addition(6, -5), multiply_by_addition_recursive(6, -5)

    print min_product(3, 5)
    print min_product(6, 8)
    print min_product(-6, 8)
    print min_product(6, -5)
