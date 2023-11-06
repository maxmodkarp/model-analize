class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return head

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    first_half = head
    second_half = slow.next
    slow.next = None 

    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    first_current = first_half
    second_current = prev
    while second_current:
        next_first = first_current.next
        next_second = second_current.next
        first_current.next = second_current
        second_current.next = next_first
        first_current = next_first
        second_current = next_second

    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

result1 = reorder_list(head1)
output1 = linked_list_to_list(result1)
print(output1)  

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)

result2 = reorder_list(head2)
output2 = linked_list_to_list(result2)
print(output2)  
