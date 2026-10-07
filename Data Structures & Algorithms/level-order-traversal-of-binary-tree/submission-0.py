# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        queue = []
        layer = 1
        if root is None:
            return []
        queue.append([root, layer])
        while queue:
            currNode, currLayer = queue.pop(0)
            if len(ret) < currLayer:
                ret.append([])
            
            ret[-1].append(currNode.val)
            if currNode.left:
                queue.append([currNode.left,currLayer + 1])
            if currNode.right:
                queue.append([currNode.right, currLayer + 1])
        return ret
        