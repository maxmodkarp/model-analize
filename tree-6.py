class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        def max_path_sum_helper(node):
            nonlocal max_sum
            if not node:
                return 0

            
            left_sum = max(max_path_sum_helper(node.left), 0)
            right_sum = max(max_path_sum_helper(node.right), 0)

            
            current_path_sum = node.val + left_sum + right_sum

            
            max_sum = max(max_sum, current_path_sum)

            
            return node.val + max(left_sum, right_sum)

        max_sum = float('-inf')
        max_path_sum_helper(root)
        return max_sum


tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.maxPathSum(tree1))  

tree2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.maxPathSum(tree2))  
