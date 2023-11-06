class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    current = head
    
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = delete_duplicates(head1)
output1 = linked_list_to_list(result1)
print(output1)  

head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = delete_duplicates(head2)
output2 = linked_list_to_list(result2)
print(output2) 
