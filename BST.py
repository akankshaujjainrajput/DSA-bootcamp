class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. Insertion
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    # 2. Deletion
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    # Utility function to find the minimum value node
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # 3. Search
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    # 4. Traversal
    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

    # Level Order Traversal (Breadth-First Search)
    def level_order(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].val, end=" ")
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Driver code to take user input and perform operations
if __name__ == '__main__':
    tree = BinaryTree()

    while True:
        print("\nOptions:")
        print("1. Insert node")
        print("2. Delete node")
        print("3. Search node")
        print("4. Inorder traversal")
        print("5. Preorder traversal")
        print("6. Postorder traversal")
        print("7. Level Order traversal")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value to insert: "))
            tree.root = tree.insert(tree.root, value)
            print(f"Inserted {value} into the tree.")

        elif choice == 2:
            value = int(input("Enter value to delete: "))
            tree.root = tree.delete(tree.root, value)
            print(f"Deleted {value} from the tree.")

        elif choice == 3:
            value = int(input("Enter value to search: "))
            result = tree.search(tree.root, value)
            if result:
                print(f"Node with value {value} found!")
            else:
                print(f"Node with value {value} not found.")

        elif choice == 4:
            print("Inorder traversal:")
            tree.inorder(tree.root)
            print()  # Newline for clarity

        elif choice == 5:
            print("Preorder traversal:")
            tree.preorder(tree.root)
            print()  # Newline for clarity

        elif choice == 6:
            print("Postorder traversal:")
            tree.postorder(tree.root)
            print()  # Newline for clarity

        elif choice == 7:
            print("Level Order traversal:")
            tree.level_order(tree.root)
            print()  # Newline for clarity

        elif choice == 8:
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")
