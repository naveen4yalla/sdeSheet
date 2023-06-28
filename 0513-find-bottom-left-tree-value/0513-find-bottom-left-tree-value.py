# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        d = -1
        value = None
        queue = []
        queue.append((root,0))
        while queue:
            for _ in range(len(queue)):
                popElement,depth = queue.pop(0)
                if popElement.right:
                    queue.append((popElement.right,depth+1))
                if popElement.left:
                    queue.append((popElement.left,depth+1))
                if depth >= d:
                         d = depth
                         value = popElement.val
        return value
            
                
        