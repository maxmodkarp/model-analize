class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    less_head = ListNode(0)  
    greater_head = ListNode(0)  
    less_current = less_head
    greater_current = greater_head

    current = head

    while current:
        if current.val < x:
            less_current.next = current
            less_current = less_current.next
        else:
            greater_current.next = current
            greater_current = greater_current.next
        current = current.next

    less_current.next = greater_head.next
    greater_current.next = None  

    return less_head.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(2)
x1 = 3

result1 = partition(head1, x1)
output1 = linked_list_to_list(result1)
print(output1)  

head2 = ListNode(2)
head2.next = ListNode(1)
x2 = 2

result2 = partition(head2, x2)
output2 = linked_list_to_list(result2)
print(output2)  
