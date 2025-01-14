class tree:
    def __init__(self , val = 0 , left = None  , right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def build_tree(self , preorder , inorder):
        if not preorder or not inorder:
            return None
        
        root = tree(preorder[0])

        i = 0
        while preorder[0] != inorder[i]:
            i+=1
        
        root.left = self.build_tree(preorder[1:i+1] , inorder[:i])
        root.right = self.build_tree(preorder[i+1:] , inorder[i+1:])

        return root
