class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []  

    def inorder(node):
        if node:
            inorder(node.left) 
            result.append(node.val)  
            inorder(node.right)  

    inorder(root)  
    return result  

root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorderTraversal(root1))  

root2 = None
print(inorderTraversal(root2))  

root3 = TreeNode(1)
print(inorderTraversal(root3))  
