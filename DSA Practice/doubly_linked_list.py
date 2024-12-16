class node:
    def __init__(self , value):
        self.value = value
        node.previous = None
        node.next = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self , value):
        new_node = node(value)
        if self.head == None:
            self.head = self.tail = new_node
            self.size += 1
            return

        temp = self.head
        self.head = new_node
        self.head.next = temp
        temp.previous = self.head
        self.size += 1

    def insert_last(self , value):
        new_node = node(value)
        if self.head == None:
            self.insert_first(new_node)
            return
        
        temp = self.tail
        self.tail = new_node
        temp.next = self.tail
        self.tail.previous = temp
        self.size += 1
    
    def insert(self , value , index):
        new_node = node(value)

        if index == 1:
            self.insert_first(value)
            return

        if index == self.size + 1:
            self.insert_last(value)
            return

        current = self.head
        for _ in range(1 , index - 1):
            current = current.next

        next_node = current.next
        current.next = new_node
        new_node.previous = current
        new_node.next = next_node
        next_node.previous = new_node
        self.size += 1
            

    def delete_first(self):
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return

        self.head = self.head.next
        self.head.previous = None
        self.size -= 1

    def delete_last(self):
        if self.size == 0:
            return

        if self.size == 1:
            self.delete_first()
            return

        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1

    def delete(self , index):
        if index == 1:
            self.delete_first()
            return

        if index == self.size:
            self.delete_last()
            return

        current_node = self.get(index)
        previous_node = current_node.previous
        next_node = current_node.next
        
        previous_node.next = next_node
        if next_node:
            next_node.previous = previous_node
        self.size -= 1


    def find(self , value):
        middle_index = self.size // 2
        current_start = self.head
        current_end = self.tail

        if(current_start.value == value):
            return 1
        
        if(current_end.value == value):
            return self.size

        for index in range(1 , middle_index + 1):
            current_start = current_start.next
            if(current_start and current_start.value == value):
                return index + 1

            current_end = current_end.previous
            if(current_end and current_end.value == value):
                return (self.size - index + 1) 
        return None

    def get(self , index):
        if index < 1 or index > self.size:
            return -1

        if index == 1:
            return self.head
        
        if index == self.size:
            return self.tail
        
        middle_index = self.size // 2

        if middle_index >= index:
            current = self. head
            for _ in range (1 , index):
                current = current.next
            return current
            
        current = self.tail
        for _ in range(self.size , index  , -1):
            current = current.previous
        return current

    def display(self , reverse = False):
        if reverse == False:
            current = self.head
            while current:
                print(str(current.value) + ' ---> ' , end='')
                current = current.next

            print('END')
            return
        
        current = self.tail
        while current:
            print(str(current.value) + ' ---> ' , end= '')
            current = current.previous

        print('START')


ddl = doubly_linked_list()
ddl.insert_first(1)
ddl.insert_first(3)
ddl.insert_first(5)
ddl.insert_first(4)
ddl.insert_first(8)
ddl.insert_last(12)
ddl.delete_last()
ddl.insert(6,4)
ddl.display()
ddl.display(reverse= True)
print(ddl.get(4).value)
print(ddl.find(4))
print(ddl.find(1))