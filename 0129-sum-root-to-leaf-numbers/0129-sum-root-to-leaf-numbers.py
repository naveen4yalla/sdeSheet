# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append((root,str(root.val)+"-"))
        result = []
        while queue:
            for _ in range(len(queue)):
                r , s = queue.pop(0)
                if r.left is None and r.right is None:
                    result.append(int(s.replace("-", "")))
                    
                if r.left:
                    queue.append((r.left,s+str(r.left.val)+'-'))
                if r.right:
                     queue.append((r.right,s+str(r.right.val)+'-'))
        return sum(result)
                    
        
        