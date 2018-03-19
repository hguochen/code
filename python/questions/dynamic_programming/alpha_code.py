"""
http://www.spoj.com/problems/ACODE/

For ecah input set, output the number of possible decodings for the input string.

Let the given string be S
Let the last index of the string be i

therefore, the number of encodings => alpha_code(S, i)

say we already know the previous i-1 string number of encodings
the recurrence relation is

alpha_code(S, i) = alpha_code(S, i-1) + alpha_code(S, i-2)

base case:

if i == 0:
    return 1 # only 1 possible alphabet
elif i == 1:
    if int(S) <= 26:
        return 2
    else:
        return 0
"""

"""
Wrong solution. Did not factor in digit 0
"""
def alpha_code(digits):
   return alpha_code_aux(digits, '')

def alpha_code_aux(prefix, suffix):
    if len(prefix) == 0 or len(prefix) == 1:
        if len(suffix) != 0 and int(suffix) <= 26:
            return 1
        else:
            return 0
    return alpha_code_aux(prefix[:-1], prefix[len(prefix)-1:]) + alpha_code_aux(prefix[:-2], prefix[len(prefix)-2:])

def ways(digits, index, memo):
    """
    DP solution
    Time: O(n) where n is length of digits
    Space: O(n)
    """
    if index >= len(digits):
        return 0
    if index == len(digits) - 1: # last index
        if int(digits[index]) == 0:
            return 0
        else:
            return 1
    elif index == len(digits) - 2: # last 2nd index
        if int(digits[index]) == 0:
            return 0
        elif int(digits[index:index+2]) in [10, 20]:
            return 1
        elif int(digits[index:index+2]) <= 26:
            return 2
        else:
            return 1

    if index not in memo:
        if int(digits[index]) == 0:
            memo[index] = 0
        elif int(digits[index:index+2]) in [10, 20]:
            memo[index] = ways(digits, index+2, memo)
        elif int(digits[index:index+2]) <= 26:
            memo[index] = ways(digits, index+1, memo) + ways(digits, index+2, memo)
        else:
            memo[index] = ways(digits, index+1, memo)
    return memo[index]

if __name__ == '__main__':
    print alpha_code('25114')
    print alpha_code('1111111111')
    print alpha_code('3333333333')

    print ways('25114', 0, {})
    print ways('1111111111', 0, {})
    print ways('3333333333', 0, {})