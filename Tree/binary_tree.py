class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_root(self , value):
        self.root = Node(value)

    def insert_left(self, value):
        if self.root:
            if not self.root.left:
                self.root.left = Node(value)
            else:
                new_node = Node(value)
                new_node.left = self.root.left
                self.root.left = new_node
        else:
            self.root = Node(value)

    def insert_right(self, value):
        if self.root:
            if not self.root.right:
                self.root.right = Node(value)
            else:
                new_node = Node(value)
                new_node.right = self.root.right
                self.root.right = new_node
        else:
            self.root = Node(value)

    # Inorder Traversal: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Postorder Traversal: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

# Example usage
tree = BinaryTree()
tree.insert_root(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.insert_right(5)

# Inorder Traversal
print("Inorder Traversal: ", end="")
tree.inorder(tree.root)  # Output: 4 2 5 1 3
print()

# Postorder Traversal
print("Postorder Traversal: ", end="")
tree.postorder(tree.root)  # Output: 4 5 2 3 1
print()
