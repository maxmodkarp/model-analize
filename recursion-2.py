class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head or not head.next:
        return head

    first_node = head
    second_node = head.next

    head = second_node
    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node

    return head


print("#1")
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = swapPairs(head)
while result:
    print(result.val, end=" -> ")
    result = result.next


print("\n")

print("#2")
head = None
result = swapPairs(head)
while result:
    print(result.val, end=" -> ")
    result = result.next


print("\n")

print("#3")
head = ListNode(1)
result = swapPairs(head)
while result:
    print(result.val, end=" -> ")
    result = result.next
