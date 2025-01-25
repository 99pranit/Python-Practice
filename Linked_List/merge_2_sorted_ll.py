class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merger(list1 , list2):
    if not list1:
        return list2

    if not list2:
        return list1
    
    head = ListNode()
    new_list = head
    
    while list1 and list2:
        if list1.val > list2.val:
            new_list.next = list2
            list2 = list2.next
        else:
            new_list.next = list1
            list1 = list1.next
        new_list = new_list.next

    if list1:
        new_list.next = list1

    if list2:
        new_list.next = list2

    return head.next
    