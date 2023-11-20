class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal):
    def build_tree(index):
        nonlocal traversal
        
        depth = 0
        while index + depth < len(traversal) and traversal[index + depth] == '-':
            depth += 1

        
        start = index + depth
        while start < len(traversal) and traversal[start].isdigit():
            start += 1
        value = int(traversal[index + depth:start])

        node = TreeNode(value)
        index = start

        
        if index < len(traversal) and traversal[index] == '-':
            node.left, index = build_tree(index)
        if index < len(traversal) and traversal[index] == '-':
            node.right, index = build_tree(index)

        return node, index

    root, _ = build_tree(0)
    return root


traversal1 = "1-2--3--4-5--6--7"
result1 = recoverFromPreorder(traversal1)


traversal2 = "1-2--3---4-5--6---7"
result2 = recoverFromPreorder(traversal2)


traversal3 = "1-401--349---90--88"
result3 = recoverFromPreorder(traversal3)

