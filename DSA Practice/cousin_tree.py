from collections import deque
class Tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class Check:
    def __init__(self):
        pass

    def is_cousin(self , root , x , y):
        if not root:
            return False
        
        unexplored_node = deque([root])
        
        while unexplored_node:
            size = len(unexplored_node)
            check_x = check_y = False
            for i in range(size):
                current = unexplored_node.popleft()

                if current.left and current.right:
                    if (current.left.val == x and current.right.val == y) or\
                          (current.left.val == y and current.right.val == x):
                        return False
                    
                if current.val == x:
                    check_x = True
                if current.val == y:
                    check_y = True
                
                if current.left:
                    unexplored_node.append(current.left)
                if current.right:
                    unexplored_node.append(current.right)
            
            if check_y and check_x:
                return True
            
            if check_y or check_x:
                return False
                
        return False


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)

x = 4
y = 3

sol = Check()
print(sol.is_cousin(root, x, y))