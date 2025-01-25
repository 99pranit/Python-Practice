class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_ll(head):
    current= head
    prev = None
    next = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
