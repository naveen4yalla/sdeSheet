# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._lowestCommonAncestor(root,p.val,q.val)
    def _lowestCommonAncestor(self,root,p,q):
        if root==None:
            return None
        if root.val>p and root.val>q:
            return self._lowestCommonAncestor(root.left,p,q)
        if root.val<p and root.val<q:
            return self._lowestCommonAncestor(root.right,p,q)
        return root
        
       