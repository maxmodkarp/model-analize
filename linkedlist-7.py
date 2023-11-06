class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

def merge_k_lists(lists):
    if not lists:
        return None

    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_list = merge_two_lists(lists[i], lists[i + 1])
                new_lists.append(merged_list)
            else:
                new_lists.append(lists[i])
        lists = new_lists

    return lists[0]

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

lists1 = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

result1 = merge_k_lists(lists1)
output1 = linked_list_to_list(result1)
print(output1)  

lists2 = []
result2 = merge_k_lists(lists2)
print(result2)  

lists3 = [
    ListNode(None)
]
result3 = merge_k_lists(lists3)
output3 = linked_list_to_list(result3)
print(output3)  
