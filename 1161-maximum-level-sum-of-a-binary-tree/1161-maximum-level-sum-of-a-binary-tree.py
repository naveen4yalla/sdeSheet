# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ls = []
        if root is None:
            return 
        ls.append([root,1])
        maxSum = float("-inf")
        level = 0
        count = 0
        while ls:
            n = len(ls)
            s = 0
            count = count + 1
            for i in range(n):
                a ,b = ls.pop(0)
                if a.left:
                    ls.append([a.left,b+1])
                if a.right:
                    ls.append([a.right,b+1])
                s = a.val + s
            if s > maxSum:
                maxSum = s
                level = count
        return level
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         ls = []
#         if root is None:
#             return
#         ls.append([root, 1])
#         maxSum = float("-inf")
#         level = 0
#         count = 0
#         while ls:
#             n = len(ls)
#             s = 0
#             count += 1
#             for _ in range(n):
#                 a, b = ls.pop(0)
#                 if a.left:
#                     ls.append([a.left, b + 1])
#                 if a.right:
#                     ls.append([a.right, b + 1])
#                 s += a.val
#             if s > maxSum:
#                 maxSum = s
#                 level = count
#         return level
                
                
                
                
                
        
        