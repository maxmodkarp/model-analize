class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next  

result1 = has_cycle(head1)
print(result1) 

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2  

result2 = has_cycle(head2)
print(result2)  

head3 = ListNode(1)  

result3 = has_cycle(head3)
print(result3)  
