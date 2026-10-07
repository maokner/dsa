# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdia = 0
        def helper(node):
            nonlocal maxdia
            if node is None:
                return -1
            
            maxLeft = 1 + helper(node.left)
            maxRight = 1 + helper(node.right)
            d = maxLeft + maxRight
            maxdia = max(maxdia, d)
            return max(maxLeft, maxRight)
        helper(root)

        return maxdia
            
        