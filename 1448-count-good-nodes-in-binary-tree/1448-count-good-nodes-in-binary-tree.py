# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxValue):
            #Base condition
            if not root:
                return 0
            #Do a preorder traversal
            result = 1 if root.val>=maxValue else 0
            #update the maximum value
            maxValue = max(maxValue,root.val)
            result = result + dfs(root.left,maxValue)
            result = result + dfs(root.right,maxValue)
            return result
        return dfs(root,root.val)
                
        