class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root):
    def dfs(node):
        nonlocal result
        
        if not node:
            return 2

        left = dfs(node.left)
        right = dfs(node.right)

        
        if left == 0 or right == 0:
            result += 1
            return 1
        elif left == 1 or right == 1:
            return 2
        else:
            return 0

    result = 0
    
    
    if dfs(root) == 0:
        result += 1
    return result


tree1 = TreeNode(0, None, TreeNode(0, None, TreeNode(0)))
print(minCameraCover(tree1))  

tree2 = TreeNode(0, None, TreeNode(0, None, TreeNode(0, TreeNode(0), None)))
print(minCameraCover(tree2))  
