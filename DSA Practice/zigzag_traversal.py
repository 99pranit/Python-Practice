from collections import deque
class tree:
    def __init__(self , value = 0 , left = None , right = None):
        self.value = value
        self.left = left
        self.right = right

class traverse:
    def __init__(self):
        pass

    def zigzag(self , root):
        if not root:
            return []
        
        unexplored_node = deque([root])
        result = []
        reverse = 1

        while unexplored_node:
            for _ in range(len(unexplored_node)):
                current_node = unexplored_node.pop() if reverse else unexplored_node.popleft()
                result.append(current_node.value)

                if reverse:
                    if current_node.right:
                        unexplored_node.appendleft(current_node.right)
                    if current_node.left:
                        unexplored_node.appendleft(current_node.left)
                else:
                    if current_node.left:
                        unexplored_node.append(current_node.left)
                    if current_node.right:
                        unexplored_node.append(current_node.right)
                
            reverse = 1 - reverse

        return result

root = tree(1, tree(2, tree(4), tree(5)), tree(3, tree(6), tree(7)))

search_instance = traverse()
print(search_instance.zigzag(root))
                    