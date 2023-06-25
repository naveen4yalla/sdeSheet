# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = []
        def helper(root):
            if root is None:
                return 
            if not root.left and not root.right:
                result.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            return
        helper(root1)
        ls = result.copy()
        result = []
        helper(root2)
        ls1 = result.copy()
        return  ls == ls1
        