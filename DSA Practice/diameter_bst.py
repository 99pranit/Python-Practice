class tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class calculate:
    def tree_diameter(self , root):
        if not root:
            return None
        
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter , left_height + right_height)

            return max(left_height , right_height) + 1
        
        height(root)
        return self.diameter
        
