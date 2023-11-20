class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(isSameTree(p1, q1))  

p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(isSameTree(p2, q2))  

p3 = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(3))
q3 = TreeNode(1, TreeNode(1), TreeNode(2))
print(isSameTree(p3, q3))  
