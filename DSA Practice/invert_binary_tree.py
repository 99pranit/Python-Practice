class tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class transform:
    def invert_tree(self , root):
        if not root:
            return None
        
        left = self.invert_tree(root.left)
        right = self.invert_tree(root.right)

        root.left = right
        root.right = left

        return root
        
