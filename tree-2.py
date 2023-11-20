class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isMirror(left, right):
        
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        return (left.val == right.val) and isMirror(left.right, right.left) and isMirror(left.left, right.right)

    
    if not root:
        return True
    
    return isMirror(root.left, root.right)


root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(root1))  

root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(isSymmetric(root2))  

root3 = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(2, TreeNode(1)))
print(isSymmetric(root3))  
