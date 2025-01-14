class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        if not root: return None

        self.count = 0
        self.result = None

        def traverse(node):
            if not node or self.result is not None:
                return
            
            traverse(node.left)
            self.count += 1

            if self.count == k:
                self.result = node.val

            traverse(node.right)
        traverse(root)
        return self.result