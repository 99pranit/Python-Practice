class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if targetSum - root.val == 0 and root.left == None and root.right == None:
            return True

        left = self.hasPathSum(root.left , targetSum - root.val) 
        right = self.hasPathSum(root.right , targetSum - root.val)

        return left or right