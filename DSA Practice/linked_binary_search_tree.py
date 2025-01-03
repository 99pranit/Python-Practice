class node:
    def __init__(self , value):
        self.value = value
        node.left = None
        node.right = None
        self.height = 0

class binary_search_tree:
    def __init__(self):
        self.root = None

    def empty_tree(self):
        self.root = None

    def height(self , node):
        if node:
            return node.height
        return -1

    def insert(self , value):
        if self.root:
            return self.place(value , self.root)
        else:
            self.root = node(value)

    def place(self , value , Node):
        if not Node:
            return node(value)
        
        if value < Node.value:
            Node.left = self.place(value , Node.left)
        else:
            Node.right = self.place(value , Node.right)
        Node.height = max(self.height(Node.left) , self.height(Node.right)) + 1
        return Node

    def inorder(self):
        current = self.root
        self.inorder_traversal(current)
        print()

    def inorder_traversal(self , current):
        if current:
            self.inorder_traversal(current.left)
            print(current.value , end= ' ')
            self.inorder_traversal(current.right)

bst = binary_search_tree()
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.inorder()