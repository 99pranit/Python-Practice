class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Initial height is 1 (leaf node)

class avl_tree:
    def __init__(self):
        self.root = None

    def height(self, current_node):
        if current_node:
            return current_node.height
        return 0  # Updated to return 0 for null nodes

    def insert(self, value):
        if not self.root:
            self.root = node(value)
        else:
            self.root = self.place(value, self.root)

    def place(self, value, parent):
        if parent is None:
            return node(value)

        if value < parent.value:
            parent.left = self.place(value, parent.left)
        else:
            parent.right = self.place(value, parent.right)

        parent.height = 1 + max(self.height(parent.left), self.height(parent.right))

        return self.balanced(parent)

    def balanced(self, current_node):
        balance_factor = self.height(current_node.left) - self.height(current_node.right)

        # Left-heavy case
        if balance_factor > 1:
            if self.height(current_node.left.left) >= self.height(current_node.left.right):
                return self.right_turn(current_node)  # Left-Left case
            else:
                current_node.left = self.left_turn(current_node.left)  # Left-Right case
                return self.right_turn(current_node)

        # Right-heavy case
        if balance_factor < -1:
            if self.height(current_node.right.right) >= self.height(current_node.right.left):
                return self.left_turn(current_node)  # Right-Right case
            else:
                current_node.right = self.right_turn(current_node.right)  # Right-Left case
                return self.left_turn(current_node)

        return current_node

    def left_turn(self, unbalanced_node):
        parent = unbalanced_node
        child = parent.right

        parent.right = child.left
        child.left = parent

        # Update heights
        parent.height = 1 + max(self.height(parent.left), self.height(parent.right))
        child.height = 1 + max(self.height(child.left), self.height(child.right))

        return child

    def right_turn(self, unbalanced_node):
        parent = unbalanced_node
        child = parent.left

        parent.left = child.right
        child.right = parent

        # Update heights
        parent.height = 1 + max(self.height(parent.left), self.height(parent.right))
        child.height = 1 + max(self.height(child.left), self.height(child.right))

        return child

    def inorder(self):
        current = self.root
        self.inorder_traversal(current)
        print()

    def inorder_traversal(self, current):
        if current:
            self.inorder_traversal(current.left)
            print(current.value, end=' ')
            self.inorder_traversal(current.right)

# Example usage
avl = avl_tree()
avl.insert(1)
avl.insert(2)
avl.insert(3)
avl.insert(4)
avl.insert(5)
avl.insert(6)
avl.insert(7)
avl.inorder()
