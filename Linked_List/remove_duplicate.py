'''
Given the head of a sorted linked list, delete all duplicates such 
that each element appears only once. Return the linked list sorted as well.
'''

def remove_duplicate(self , head):
    if not head:
        return None

    dummy = head

    while dummy.next:
        if dummy.val == dummy.next.val:
            dummy.next = dummy.next.next
        else:
            dummy = dummy.next
    
    return head