import java.util.Scanner;

class Queue {
    private int front, rear, capacity;
    private int[] queue;

    // Constructor to initialize the queue
    public Queue(int size) {
        capacity = size;
        front = rear = 0;
        queue = new int[capacity];
    }

    // Method to add an element to the queue
    public void enqueue(int data) {
        if (isFull()) {
            System.out.println("Queue is full, cannot enqueue.");
            return;
        }
        queue[rear] = data;
        rear++;
    }

    // Method to remove an element from the queue
    public void dequeue() {
        if (isEmpty()) {
            System.out.println("Queue is empty, cannot dequeue.");
            return;
        }
        System.out.println("Removed: " + queue[front]);
        for (int i = 0; i < rear - 1; i++) {
            queue[i] = queue[i + 1];
        }
        rear--;
    }

    // Method to view the front element of the queue
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty, nothing to peek.");
            return -1;
        }
        return queue[front];
    }

    // Method to check if the queue is empty
    public boolean isEmpty() {
        return front == rear;
    }

    // Method to check if the queue is full
    public boolean isFull() {
        return rear == capacity;
    }

    // Method to print the queue
    public void printQueue() {
        if (isEmpty()) {
            System.out.println("Queue is empty.");
            return;
        }
        for (int i = front; i < rear; i++) {
            System.out.print(queue[i] + " ");
        }
        System.out.println();
    }
}

// Main class to test the Queue with user input
public class QueueImplementation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the queue: ");
        int size = scanner.nextInt();
        Queue q = new Queue(size);

        while (true) {
            System.out.println("\nChoose an operation: ");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Print Queue");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the value to enqueue: ");
                    int value = scanner.nextInt();
                    q.enqueue(value);
                    break;
                case 2:
                    q.dequeue();
                    break;
                case 3:
                    int frontElement = q.peek();
                    if (frontElement != -1) {
                        System.out.println("Front element is: " + frontElement);
                    }
                    break;
                case 4:
                    System.out.println("Queue contents:");
                    q.printQueue();
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
