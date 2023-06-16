# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None≥
#         self.right = None

class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(node):
            if not node:
                return False
            left = recursion(node.left)
            
            right = recursion(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ans = node
                
            return mid or left or right
        
        recursion(root)
        return self.ans
        