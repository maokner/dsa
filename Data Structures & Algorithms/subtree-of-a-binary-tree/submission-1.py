# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # sametree takes q as the subroot
        self.ret = False
        def sameTree(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            else:
                return False
            

        def dfs(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)
        return dfs(root)
            


        