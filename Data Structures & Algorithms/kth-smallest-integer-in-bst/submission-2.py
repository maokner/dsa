# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []
        self.numSeen = 0
        self.ret = -1
        def dfs(node):
            if not node or self.ret != -1:
                return
            dfs(node.left)
            self.numSeen += 1
            if self.numSeen == k:
                self.ret = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.ret
        