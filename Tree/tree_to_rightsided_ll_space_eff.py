class Tree:
    def __init__(self, left = None , right = None, val = 0 , next = None):
        self.left = left
        self.right = right
        self.val = val
        self.next = next

class connect_tree:
    def __init__(self):
        pass

    def connect(self , root):
        if not root:
            return []
        
        level_start = root
        while level_start.left:
            current = level_start
            while current:
                current.left.next = current.right

                if current.next:
                    current.right.next = current.next.left

                current = current.next
            
            level_start = level_start.left

        return root
    
    def print_levels(self , root):
        start = root
        while start:
            current = start
            while current:
                print(str(current.val) + '--->' , end='')
                current = current.next
            print('end')
            start = start.left
    

root = Tree(
    val=1,
    left=Tree(
        val=2,
        left=Tree(val=4),
        right=Tree(val=5)
    ),
    right=Tree(
        val=3,
        left=Tree(val=6),
        right=Tree(val=7)
    )
)
connector = connect_tree()

connector.connect(root)

connector.print_levels(root)
