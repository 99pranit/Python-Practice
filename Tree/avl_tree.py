class node:
    def __init__(self , value):
        self.value = value
        node.left = None
        node.right = None
        self.height = 0

class avl_tree:
    def __init__(self):
        self.root = None

    def height(self , current_node):
        if current_node:
            return current_node.height
        return -1
    
    def insert(self , value):
        if self.root:
            return self.place(value , self.root)
        
        self.root = node(value)

    def place(self , value , parent):
        if parent == None:
            new_node = node(value)
            return new_node

        if parent.value < value:
            parent.left = self.place(value , parent.left)
        else:
            parent.right = self.place(value , parent.right)

        parent.height = max(self.height(parent.left) , self.height(parent.right)) + 1

        return parent

    def balanced(self , current_node):
        if self.height(current_node.left) - self.height(current_node.right) > 1: #left_major
            if self.height(current_node.left.left) - self.height(current_node.left.right) < 0: #left_right
                current_node.left = self.left_turn(current_node.left)
                return  self.right_turn(current_node)
            return self.right_turn(current_node)
        else: #right_major
            if self.height(current_node.right.right) - self.height(current_node.right.left) < 0: #right_left
                current_node.right = self.left_turn(current_node.right)
                return  self.right_turn(current_node)
            return self.right_turn(current_node)

    def left_turn(self , unbalanced_node):
        parent = unbalanced_node
        child = parent.right

        parent.right = child.left
        child.left = parent

        parent.height = max(self.height(parent.left) , self.height(parent.right)) + 1
        child.height = max(self.height(child.left) , self.height(child.right)) + 1
        return child

    def right_turn(self , unbalanced_node):
        parent = unbalanced_node
        child = parent.left

        parent.left = child.right
        child.right = parent

        parent.height = max(self.height(parent.left) , self.height(parent.right)) + 1
        child.height = max(self.height(child.left) , self.height(child.right)) + 1

        return child


    def inorder(self):
        current = self.root
        self.inorder_traversal(current)
        print()

    def inorder_traversal(self , current):
        if current:
            self.inorder_traversal(current.left)
            print(current.value , end= ' ')
            self.inorder_traversal(current.right)


avl = avl_tree()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)
avl.insert(7)
avl.inorder()