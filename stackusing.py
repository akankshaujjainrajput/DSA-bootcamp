# Node class to define each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Method to push an element to the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top  # Link the new node to the previous top
        self.top = new_node  # Update the top to be the new node
        print(f"Pushed {data} to stack")

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        popped_node = self.top  # Get the top node
        self.top = self.top.next  # Move the top to the next node
        print(f"Popped {popped_node.data} from stack")
        return popped_node.data

    # Method to peek the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    # Method to display the stack elements
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements:")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Testing the stack implementation
if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    print("Top element is", stack.peek())

    stack.pop()
    stack.display()

    print("Top element is", stack.peek())
