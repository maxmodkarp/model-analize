class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    def inorder_traversal(node):
        
        nonlocal k, result

        if node is None:
            return

        
        inorder_traversal(node.left)

        
        k -= 1
        if k == 0:
            result = node.val
            return

        
        inorder_traversal(node.right)

    result = None
    inorder_traversal(root)
    return result


root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kthSmallest(root1, 1))  

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kthSmallest(root2, 3))  
