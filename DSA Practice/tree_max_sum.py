class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        if not root:
            return None
        
        self.maxsum = float('-inf')

        def helper(root):
            if not root:
                return 0
            
            left = max(0 , helper(root.left))
            right = max(0 , helper(root.right))

            self.maxsum = max(self.maxsum , left + right + root.val)
            return max(left , right) + root.val
        
        helper(root , 0)
        return self.maxsum