/**
 * This class defines an integer stack that can hold 10 values
 */
class Stack {
    int stack[] = new int[10];
    int tos;

    Stack() {
        tos = -1;
    }

    void push(int item) {
        if (tos == 9) {
            System.out.println("Stack is full.");
        } else {
            stack[++tos] = item;
        }
    }

    int pop() {
        if (tos < 0) {
            System.out.println("Stack underflow.");
            return 0;
        } else {
            return stack[tos--];
        }
    }

    void printStack() {
        for (int val : stack) {
            System.out.print(val + " ");
        }
        System.out.println();
    }
}

class StackDemo {
    public static void main(String args[]) {
        Stack stack = new Stack();
        stack.push(9);
        stack.push(8);
        stack.printStack();
        System.out.println(stack.pop());
        System.out.println(stack.pop());
    }
}