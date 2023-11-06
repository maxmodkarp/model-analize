class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    if node is None or node.next is None:
        return

    node.val = node.next.val
    node.next = node.next.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

head1 = ListNode(4)
head1.next = ListNode(5)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(9)
node_to_delete1 = head1.next  

delete_node(node_to_delete1)
output1 = linked_list_to_list(head1)
print(output1) 

head2 = ListNode(4)
head2.next = ListNode(5)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(9)
node_to_delete2 = head2.next.next  

delete_node(node_to_delete2)
output2 = linked_list_to_list(head2)
print(output2)  
