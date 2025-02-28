class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        if not root:
            return None

        def helper(root , num):
            if not root:
                return 0
            
            num =num * 10 + root.val

            if not root.left and not root.right:
                return num

            return helper(root.left , num) + helper(root.right , num)
        
        return helper(root)