from collections import deque
class tree:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

class view:

    def right_side_view(self , root):
        if not root:
            return []
        
        unexplore_node = deque([root])
        result = []
        while unexplore_node:
            for _ in range(len(unexplore_node)):
                current = unexplore_node.popleft()

                if current.left:
                    unexplore_node.append(current.left)

                if current.right:
                    unexplore_node.append(current.right)

            result.append(current.val)

        return result
    
root = tree(1, tree(2, tree(4), tree(5)), tree(3, tree(6), tree(7)))

view_obj = view()
print(view_obj.right_side_view(root))