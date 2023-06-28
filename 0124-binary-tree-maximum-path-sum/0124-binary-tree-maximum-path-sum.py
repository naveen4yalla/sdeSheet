# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxpath = [float("-inf")]
        def postorder(root):
            if root is None:
                return 0
            leftval = max(postorder(root.left),0)
            rightval = max(postorder(root.right),0)
            maxpath[0] = max(leftval+rightval+root.val,maxpath[0])
            return max(leftval+root.val , rightval+root.val)
        postorder(root)
        return maxpath[0]
            
            
        
        