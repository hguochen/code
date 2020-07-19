class Stack {
    private int stck[];
    private int tos;

    // allocate and initialize stack
    Stack(int size) {
        stck = new int[size];
        tos = -1;
    }

    // push an item onto stack
    void push(int item) {
        if (tos == stck.length - 1) {
            System.out.println("Stack is full.");
        } else {
            stck[++tos] = item;
        }
    }

    // pop an item from the stack
    int pop() {
        if ( tos < 0) {
            System.out.println("Stack underflow.");
            return -1; // should not return an integer here, might confuse with actual item return. throw an error
        } else {
            return stck[tos--];
        }
    }
}

public class TestStack2 {
    public static void main(String[] args) {
        Stack myStack1 = new Stack(5);
        Stack myStack2 = new Stack(8);

        // push numbers onto the stack
        for (int i = 0; i < 5; i++) {
            myStack1.push(i);
        }
        for (int i = 0; i < 8; i++) {
            myStack2.push(i);
        }

        // pop numbers off the stack
        System.out.println("stack in mystack1:");
        for (int i = 0; i < 5; i++) {
            System.out.println(myStack1.pop());
        }
        System.out.println("stack in mystack2:");
        for (int i = 0; i < 8; i++) {
            System.out.println(myStack2.pop());
        }
    }
}
