class tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class flatten:
    def to_linkedlist(self , root):
        if not root:
            return None
        
        current = root
        while current:
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right

                temp.right = current.right
                current.right = current.left
                current.left = None
            current = current.right

        return root
