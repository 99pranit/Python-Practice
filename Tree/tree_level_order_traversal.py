from collections import deque
class tree:
    def __init__(self , value = 0 , left = None , right = None):
        self.value = value
        self.left = left
        self.right = right

class search:
    def __init__(self):
        pass

    def level_order(self , root):
        if not root:
            return []
        
        unexplored_node = deque([root])
        result = []
        
        while unexplored_node:
            dummmy_result = []
            size = len(unexplored_node)

            for _ in range(len(unexplored_node)):
                current_node = unexplored_node.popleft()
                dummmy_result.append(current_node.value)

                if current_node.left:
                    unexplored_node.append(current_node.left)

                if current_node.right:
                    unexplored_node.append(current_node.right)
            
            result.append(dummmy_result)

        return result
    
root = tree(1, tree(2, tree(4), tree(5)), tree(3, tree(6), tree(7)))

search_instance = search()
print(search_instance.level_order(root))
