"""
https://www.geeksforgeeks.org/expression-evaluation/
Evaluate an expression represented by a String. Expression can contain parentheses,
you can assume parentheses are well-matched. For simplicity, you can assume only binary
operations allowed are +,-,*,/. Arithmetic expression can be written in one of three forms.
"""

def expression_evaluation(string):
    """
    Time: O(n)
    Space: O(n)
    where n is the size of the string

    1. While there are still tokens to be read in,
       1.1 Get the next token.
       1.2 If the token is:
           1.2.1 A number: push it onto the value stack.
           1.2.2 A variable: get its value, and push onto the value stack.
           1.2.3 A left parenthesis: push it onto the operator stack.
           1.2.4 A right parenthesis:
             1 While the thing on top of the operator stack is not a 
               left parenthesis,
                 1 Pop the operator from the operator stack.
                 2 Pop the value stack twice, getting two operands.
                 3 Apply the operator to the operands, in the correct order.
                 4 Push the result onto the value stack.
             2 Pop the left parenthesis from the operator stack, and discard it.
           1.2.5 An operator (call it thisOp):
             1 While the operator stack is not empty, and the top thing on the
               operator stack has the same or greater precedence as thisOp,
               1 Pop the operator from the operator stack.
               2 Pop the value stack twice, getting two operands.
               3 Apply the operator to the operands, in the correct order.
               4 Push the result onto the value stack.
             2 Push thisOp onto the operator stack.
    2. While the operator stack is not empty,
        1 Pop the operator from the operator stack.
        2 Pop the value stack twice, getting two operands.
        3 Apply the operator to the operands, in the correct order.
        4 Push the result onto the value stack.
    3. At this point the operator stack should be empty, and the value
       stack should have only one value in it, which is the final result.

    """
    if not string:
        return
    expr = string.split()
    numbers, operators = [], []

    for i in xrange(len(expr)):
        if expr[i].isdigit():
            numbers.append(int(expr[i]))
        elif expr[i] == "(":
            operators.append(expr[i])
        elif expr[i] == ")":
            while operators[-1] != "(":
                op = operators.pop()
                value1 = numbers.pop()
                value2 = numbers.pop()
                result = perform_operation(op, value1, value2)
                numbers.append(result)
            if operators[-1] == "(":
                operators.pop()
        elif expr[i] == "+" or expr[i] == "-" or expr[i] == "*" or expr[i] == "/":
            while len(operators) > 0 and has_precedence(expr[i], operators[-1]):
                op = operators.pop()
                value1 = numbers.pop()
                value2 = numbers.pop()
                numbers.append(perform_operation(op, value1, value2))
            operators.append(expr[i])
    while len(operators) > 0:
        op = operators.pop()
        value1 = numbers.pop()
        value2 = numbers.pop()
        res = perform_operation(op, value1, value2)
        numbers.append(res)
    return numbers.pop()

def has_precedence(op1, op2):
    """
    Returns true if op2 has higher or same precedence as op1,
    Otherwise returns false.
    """
    if op2 == "(" or op2 == ")":
        return False
    if (op1 == "*" or op1 == "/") and (op2 == "+" or op2 == "-"):
        return False
    else:
        return True

def perform_operation(op, value1, value2):
    value1 = int(value1)
    value2 = int(value2)
    if op == "+":
        return value1 + value2
    elif op == "-":
        return value1 - value2
    elif op == "*":
        return value1 * value2
    elif op == "/":
        if value1 > value2:
            return value1 / value2
        return value2 / value1

if __name__ == '__main__':
    expr1 = "10 + 2 * 6" # 22
    expr2 = "100 * 2 + 12" # 212
    expr3 = "100 * ( 2 + 12 )" # 1400
    expr4 = "100 * ( 2 + 12 ) / 14" # 100
    expr5 = "+ 3 4"
    expr6 = "3 4 + "

    print expression_evaluation(expr1)
    print expression_evaluation(expr2)
    print expression_evaluation(expr3)
    print expression_evaluation(expr4)
    print expression_evaluation(expr5)
    print expression_evaluation(expr6)
