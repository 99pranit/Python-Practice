class TreeNode:
    def __init__(self, x = 0 , left = None , right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left , p , q)
        right = self.lowestCommonAncestor(root.right , p , q)

        if left and right:
            return root
        
        return left if left else right