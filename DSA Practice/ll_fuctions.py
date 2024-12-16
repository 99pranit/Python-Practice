class node:
    def __init__(self , value):
        self.value = value
        node.next = None

class ll:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def insert_first(self , value):
        new_node = node(value)
        if self.head == None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def insert_last(self,value):
        new_node = node(value)
        if self.head == None:
            self.head = self.tail = new_node
            self.size += 1
        else:   
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1



    def insert_at_index(self , value , index):
        if self.head == None:
            return self.insert_first(value) 
        elif index == self.size:
            return self.insert_last(value)
        else:
            self.head = self.insert_at_index_rec(value , index , self.head)

    def insert_at_index_rec(self , value , index , current):
        if index == 0:
            new_node = node(value)
            new_node.next = current
            self.size = self.size + 1
            return new_node
        else:
            current.next = self.insert_at_index_rec(value , index - 1 , current.next)
            return current
    
    def display(self):
        current = self.head
        while current:
            print(str(current.value) + " ---> ", end="")
            current = current.next
        print('END')

    def remove_duplicate(self):
        current = self.head

        while current:
            if current.value == current.next.value:
                current.next = current.next.next
            current = current.next

    def merge_ll(self , ll1 , ll2):
        c1 = ll1.head
        c2 = ll2.head

        if self.head == None and c1.value <= c2.value:
            self.head = self.tail = c1
            c1 = c1.next
        else:
            self.head = self.tail = c2
            c2 = c2.next

        current = self.head
        while c1 and c2:
            if c1.value > c2.value:
                current.next = c2
                c2 = c2.next
            else:
                current.next = c1
                c1 = c1.next
            current = current.next

        while c1:
            current.next = c1
            c1 = c1.next
            current = current.next

        while c2:
            current.next = c2
            c2 = c2.next
            current = current.next
        return current
    
    def merger(self , ll1 , ll2):
        dummy_ll = node()
        dummy = dummy_ll.head

        if dummy_ll.head == None and ll1.value > ll2.value:
            dummy_ll.head = ll2
            ll2 = ll2.next
        else:
            dummy_ll.head == ll1
            ll1 = ll1.next

        while ll1 and ll2:
            if ll1.value > ll2.value:
                dummy.next = ll2
                ll2 = ll2.next
            else:
                dummy.next = ll1
                ll1 = ll1.next
            dummy = dummy.next

        while ll1:
            dummy.next = ll1
            dummy = dummy.next

        while ll2:
            dummy.next = ll2
            dummy = dummy.next
        return dummy_ll


        
    
    def middle(self , head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge_sort(self , head):
        if not head or not head.next:
            return head

        left = head
        mid = self.middle(head)
        right = mid

        ll1 = self.merge_sort(left)
        ll2 = self.merge_sort(right)

        merger = self.merge_ll(ll1 , ll2)

        return merger



        
ll1 = ll()
ll1.insert_first(1)
ll1.insert_first(1)
ll1.insert_last(4)
ll1.insert_last(4)
ll1.insert_at_index(3,2)
ll1.remove_duplicate()
ll1.display()
print(ll1.middle(ll1.head).value)

ll2 = ll()
ll2.insert_last(1)
ll2.insert_last(3)
ll2.insert_last(5)
ll2.insert_last(7)
ll2.display()

ll3 = ll()
ll3.insert_last(2)
ll3.insert_last(4)
ll3.insert_last(6)
ll3.insert_last(8)
ll3.display()

ll4 = ll()
ll4.merge_ll(ll2,ll3)
ll4.display()

ll5 = ll()
ll5.insert_last(2)
ll5.insert_last(1)
ll5.insert_last(3)
ll5.insert_last(5)
ll5.insert_last(4)
ll5.insert_last(3)
ll5.display()
ll5.merge_sort(ll5.head)
ll5.display