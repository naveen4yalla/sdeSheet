# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1

            return max(left,right)
        return helper(root)
        