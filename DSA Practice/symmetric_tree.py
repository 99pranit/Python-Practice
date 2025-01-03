from collections import deque
class Tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class Type:
    def __init__(self):
        pass

    def is_symmetric(self,root):
        if not root:
            return False
        
        unexplored = deque([(root.left , root.right)])

        while unexplored:
            t1 , t2 = unexplored.popleft()

            if not t1 and not t2:
                continue

            if not t1 or not t2:
                return False
            
            if t1.val != t2.val:
                return False
            
            unexplored.append((t1.left , t2.right))
            unexplored.append((t1.right , t2.left))
        return True

root = Tree(1)
root.left = Tree(2, Tree(3), Tree(4))
root.right = Tree(2, Tree(4), Tree(3))

sol = Type()
print(sol.is_symmetric(root))       
                