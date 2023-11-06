class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_group(head, k):
        prev = None
        current = head
        while k > 0:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            k -= 1
        return prev, current

    def count_nodes(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    count = count_nodes(head)
    if count < k:
        return head

    new_head, remaining = reverse_group(head, k)
    head.next = reverse_k_group(remaining, k)

    return new_head

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
head1.next.next.next.next = ListNode(5)
k1 = 2

result1 = reverse_k_group(head1, k1)
output1 = linked_list_to_list(result1)
print(output1)  

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
k2 = 3

result2 = reverse_k_group(head2, k2)
output2 = linked_list_to_list(result2)
print(output2)  
