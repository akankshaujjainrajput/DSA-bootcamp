class Node:
    def __init__(self, data):
        self.data = data  # Stores the data
        self.next = None  # Points to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def add_node(self, data):
        """Adds a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Node with data {data} added as the head node")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Node with data {data} added to the end of the list")

    def delete_node(self, data):
        """Deletes the first node with the given data."""
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            print(f"Node with data {data} not found")
        else:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            print(f"Node with data {data} deleted from the list")

    def display(self):
        """Displays all nodes in the list."""
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            print("Singly Linked List elements:", end=" ")
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  # Indicate the end of the list


# Main program to use the SinglyLinkedList
def main():
    sll = SinglyLinkedList()
    while True:
        print("\n1. Add Node\n2. Delete Node\n3. Display List\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to add: "))
            sll.add_node(data)
        elif choice == 2:
            data = int(input("Enter data to delete: "))
            sll.delete_node(data)
        elif choice == 3:
            sll.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()
