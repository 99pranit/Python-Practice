class tree:
    def __init__(self , value , left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class calculate:
    def max_depth(self , root):
        if not root:
            return 0

        return max(self.max_depth(root.left),  self.max_depth(root.right)) + 1