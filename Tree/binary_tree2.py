class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        pass

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(str(root.value) + " ", end="")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(str(root.value) + " ", end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.value) + " ", end="")


tree = Node(2)
tree.left = Node(3)
tree.right = Node(4)
tree.left.left = Node(5)
tree.left.right = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)


bt = BinaryTree()

print("In-order traversal:")
bt.inorder(tree)  
print("\nPre-order traversal:")
bt.preorder(tree)
print("\nPost-order traversal:")
bt.postorder(tree)
