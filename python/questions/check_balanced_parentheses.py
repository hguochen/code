"""
https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

"""

def check_balanced_parentheses(string):
    if not string:
        return False
    paren = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for i in xrange(len(string)):
        if string[i] in paren.keys():
            stack.append(string[i])
        elif string[i] in paren.values():
            if len(stack) < 1:
                return False
            bracket = stack.pop()
            if string[i] != paren[bracket]:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    str1 = "{()}[]"
    print check_balanced_parentheses(str1)