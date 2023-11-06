class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head):
    if not head:
        return None

    carry = 0
    current = head
    prev = None

    while current.next:
        current = current.next

    while current:
        current.val = current.val * 2 + carry
        carry = current.val // 10
        current.val = current.val % 10

        if not current.next and carry:
            current.next = ListNode(carry)
            carry = 0

        prev = current
        current = current.next

    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

head1 = ListNode(1)
head1.next = ListNode(8)
head1.next.next = ListNode(9)

result1 = double_linked_list(head1)
output1 = linked_list_to_list(result1)
print(output1)  

head2 = ListNode(9)
head2.next = ListNode(9)
head2.next.next = ListNode(9)

result2 = double_linked_list(head2)
output2 = linked_list_to_list(result2)
print(output2)  
