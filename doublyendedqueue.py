# Node class for each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Deque class using a doubly linked list
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    # Method to check if the deque is empty
    def is_empty(self):
        return self.front is None

    # Method to add an element at the front
    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Added {data} to the front")

    # Method to add an element at the rear
    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(f"Added {data} to the rear")

    # Method to remove an element from the front
    def remove_front(self):
        if self.is_empty():
            print("Deque Underflow! Cannot remove from the front.")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        print(f"Removed {removed_data} from the front")
        return removed_data

    # Method to remove an element from the rear
    def remove_rear(self):
        if self.is_empty():
            print("Deque Underflow! Cannot remove from the rear.")
            return None
        removed_data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        print(f"Removed {removed_data} from the rear")
        return removed_data

    # Method to display elements from front to rear
    def display(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            current = self.front
            print("Deque elements from front to rear:")
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

# Function to take user input and interact with the deque
def deque_operations():
    deque = Deque()

    while True:
        print("\n--- Double Ended Queue Operations ---")
        print("1. Add to Front")
        print("2. Add to Rear")
        print("3. Remove from Front")
        print("4. Remove from Rear")
        print("5. Display Deque")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to add to the front: "))
            deque.add_front(data)
        elif choice == 2:
            data = int(input("Enter data to add to the rear: "))
            deque.add_rear(data)
        elif choice == 3:
            deque.remove_front()
        elif choice == 4:
            deque.remove_rear()
        elif choice == 5:
            deque.display
