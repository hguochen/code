"""
CtCi
3.5 Write a program to sort a stack such that the smallest items are on top. 
You can use an additional temporary stack, but you may not copy the elements into
any other data structure(such as an array), The stack supports the following
operations: push, pop, peek and isEmpty.
"""

def sort_stack(stack):
    """
    Time: O(n^2)
    Space: O(n)
    where n is the size of the stack
    """
    if len(stack) <= 1:
        return stack
    aux = []
    while len(stack) > 0:
        value = stack.pop()
        if len(aux) < 1:
            aux.append(value)
            continue
        while len(aux) > 0 and value < aux[-1]:
            stack.append(aux.pop())
        aux.append(value)
    while len(aux) > 0:
        stack.append(aux.pop())
    return stack

if __name__ == '__main__':
    stack1 = [25, 12, 22, 11, 64]
    stack2 = [4,3,2,10,12,1,5,6]
    
    print sort_stack(stack1)
    print sort_stack(stack2)
