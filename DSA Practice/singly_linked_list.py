class node:
    def __init__(self, value):
        self.value = value
        node.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self , value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node

        if(self.tail == None):
            self.tail = self.head
        
        self.size += 1

    def insert_last(self, value):
        new_node = node(value)
        if (self.head == None):
            self.head = self.tail = new_node
            self.size += 1
            return
        
        temp = self.tail
        self.tail = new_node
        temp.next = self.tail
        self.size += 1

    def insert(self, value, index):
        new_node = node(value)
        if index == 1:
            ll.insert_first(value)
            return
        
        if index == self.size:
            ll.insert_last(value)
            return
        
        temp = ll.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1
        return
        

    def delete_first(self):
        temp = self.head.value
        self.head = self.head.next
        self.size -= 1
        if(self.head == None):
            self.tail = None

        return 
    
    def delete_last(self):
        if self.head == None:
            return
        
        if self.size == 1:
            temp = self.head.value
            self.head = self.tail = None
            self.size -= 1
            return 
        
        temp = self.tail.value
        second_element = ll.get(self.size - 1)
        self.tail = second_element
        self.tail.next = None
        return

    def delete(self, index):
        if index == self.size:
            ll.delete_last()
            return
        
        if index == 1:
            ll.delete_first()
            return
        
        previous = ll.get(index - 1)
        previous.next = previous.next.next
        self.size -= 1
        return



    def get(self , index):
        current = self.head
        if index == 1:
            return self.head
        
        if index == self.size:
            return self.tail
        
        for i in range(1 , index):
            current = current.next

        return current

    def find(self,value):
        current = self.head
        index = 1

        while(current != None):
            if (current.value == value):
                return index
            current = current.next
            index += 1

        return None

    def display(self):
        current = self.head

        while current:
            print(str(current.value) + ' ---> ' , end="")
            current = current.next
        
        print('END')


ll = linkedlist()
ll.insert_first(2)
ll.insert_first(8)
ll.insert_first(6)
ll.insert_first(4)
ll.insert_first(12)
ll.insert_last(13)
print(ll.get(3).value)
ll.delete_last()
ll.insert_last(14)
ll.insert(5,3)
ll.delete(4)
ll.display()
print(ll.find(8))