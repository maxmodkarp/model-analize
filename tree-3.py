class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    
    if not root:
        return None

    
    root.left, root.right = root.right, root.left

    
    invertTree(root.left)
    invertTree(root.right)

    return root


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
result1 = invertTree(root1)

print(result1.val, result1.left.val, result1.right.val, result1.left.left.val, result1.left.right.val,
      result1.right.left.val, result1.right.right.val)

root2 = TreeNode(2, TreeNode(1), TreeNode(3))
result2 = invertTree(root2)

print(result2.val, result2.left.val, result2.right.val)

root3 = None
result3 = invertTree(root3)

print(result3)
