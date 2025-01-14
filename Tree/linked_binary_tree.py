class node:
    def __init__(self , value):
        self.value = value
        node.left = None
        node.right = None

class binary_tree:
    def __init__(self):
        self.root = None

    def insert_root(self , value):
        if self.root:
            print('Root already present.')
            return self.root
        else:
            new_node = node(value)
            self.root = new_node
            return self.root

    def insert_left(self , value , left_of_node):
        new_node = node(value)

        if left_of_node.left:
            print('Left branch already present.')
            return
        
        if self.root:
            left_of_node.left = new_node
        else:
            print(f'Root not present. Root is set to {new_node.value}.')
            self.root = new_node

    def insert_right(self , value , right_of_node):
        new_node = node(value)

        if right_of_node.right:
            print('Right branch already present.')
            return
        
        if self.root:
            right_of_node.right = new_node
        else:
            print(f'Root not present. Root is set to {new_node.value}.')
            self.root = new_node

    def inorder_traversal(self , node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value , end= ' ')
            self.inorder_traversal(node.right)

    def inorder(self):
        root = self.root
        self.inorder_traversal(root)
        print()

    def preorder_traversal(self , node):
        if node:
            print(node.value , end= ' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def preorder(self):
        root = self.root
        self.preorder_traversal(root)
        print()

    def postorder_traversal(self , node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value , end= ' ')

    def postorder(self):
        root = self.root
        self.postorder_traversal(root)
        print()

tree = binary_tree()
root = tree.insert_root(1)
tree.insert_left(2 , root)
tree.insert_right(3 , root)
tree.insert_left(4 , root.left)
tree.insert_right(5 , root.left)
tree.insert_left(6 , root.right)
tree.insert_right(7 , root.right)
tree.inorder()
tree.postorder()
tree.preorder()