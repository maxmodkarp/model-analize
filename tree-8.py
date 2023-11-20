from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    
    columns = defaultdict(list)

    
    queue = deque([(root, 0, 0)])  
    while queue:
        node, row, col = queue.popleft()
        columns[col].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    
    result = []
    for col in sorted(columns):
        result.append([val for row, val in sorted(columns[col])])

    return result


tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(verticalTraversal(tree1))


tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(verticalTraversal(tree2))

