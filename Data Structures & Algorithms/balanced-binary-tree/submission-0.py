# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(node):
            if self.res == False:
                return 0
            if node == None:
                return 0
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            if abs(maxLeft - maxRight) > 1:
                self.res = False
            return 1 + max(maxLeft, maxRight)

        dfs(root)
        return self.res
            
        