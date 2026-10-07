# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdia = 0
        def helper(node):
            if node is None:
                return 0
            
            maxLeft = helper(node.left)
            maxRight = helper(node.right)
            d = maxLeft + maxRight
            self.maxdia = max(self.maxdia, d)
            return 1 + max(maxLeft, maxRight)
        helper(root)

        return self.maxdia
            
        