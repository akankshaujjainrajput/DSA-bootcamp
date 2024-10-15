import java.util.Scanner;

class Stack {
    private int top;
    private int capacity;
    private int[] stack;

    // Constructor to initialize the stack
    public Stack(int size) {
        capacity = size;
        stack = new int[capacity];
        top = -1; // Indicates that the stack is empty
    }

    // Method to add an element to the stack
    public void push(int data) {
        if (isFull()) {
            System.out.println("Stack is full, cannot push " + data);
            return;
        }
        stack[++top] = data; // Increment top and add the new element
        System.out.println(data + " pushed onto stack.");
    }

    // Method to remove an element from the stack
    public void pop() {
        if (isEmpty()) {
            System.out.println("Stack is empty, cannot pop.");
            return;
        }
        System.out.println("Popped: " + stack[top--]); // Return the top element and decrement top
    }

    // Method to view the top element of the stack
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty, nothing to peek.");
            return -1; // Indicates empty stack
        }
        return stack[top]; // Return the top element
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Method to check if the stack is full
    public boolean isFull() {
        return top == capacity - 1;
    }

    // Method to print the stack
    public void printStack() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return;
        }
        System.out.print("Stack elements: ");
        for (int i = 0; i <= top; i++) {
            System.out.print(stack[i] + " ");
        }
        System.out.println();
    }
}

// Main class to test the Stack with user input
public class StackImplementation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the stack: ");
        int size = scanner.nextInt();
        Stack stack = new Stack(size);

        while (true) {
            System.out.println("\nStack Operations");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Print Stack");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the value to push: ");
                    int value = scanner.nextInt();
                    stack.push(value);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    int topElement = stack.peek();
                    if (topElement != -1) {
                        System.out.println("Top element is: " + topElement);
                    }
                    break;
                case 4:
                    stack.printStack();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice, please try again.");
            }
        }
    }
}
