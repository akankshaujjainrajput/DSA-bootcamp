class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

class AVLTree:
    # Function to get the height of the node
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Function to get the balance factor of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    # Right rotate subtree rooted with y
    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1

        # Return new root
        return x

    # Left rotate subtree rooted with x
    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) + 1

        # Return new root
        return y

    # Insert a node into the AVL Tree
    def insert(self, root, key):
        # Perform the normal BST insertion
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the root node
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1

        # Get the balance factor to check whether the node became unbalanced
        balance = self.getBalance(root)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Find the node with the minimum value
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node from the AVL Tree
    def delete(self, root, key):
        # Perform the normal BST deletion
        if not root:
            return root
        elif key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        # If the tree had only one node then return
        if root is None:
            return root

        # Update the height of the current node
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1

        # Get the balance factor to check whether the node became unbalanced
        balance = self.getBalance(root)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Left Right Case
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Right Left Case
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Search for a node
    def search(self, root, key):
        if not root or root.val == key:
            return root
        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # In-order Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    # Pre-order Traversal
    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    # Post-order Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

def main():
    avl = AVLTree()
    root = None

    while True:
        print("\nOperations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            key = int(input("Enter value to insert: "))
            root = avl.insert(root, key)
        elif choice == 2:
            key = int(input("Enter value to delete: "))
            root = avl.delete(root, key)
        elif choice == 3:
            key = int(input("Enter value to search: "))
            found = avl.search(root, key)
            if found:
                print(f"Node {key} found in the AVL Tree.")
            else:
                print(f"Node {key} not found.")
        elif choice == 4:
            print("Inorder Traversal: ", end='')
            avl.inorder(root)
            print()
        elif choice == 5:
            print("Preorder Traversal: ", end='')
           
if __name__ == "__main__":
    main()
