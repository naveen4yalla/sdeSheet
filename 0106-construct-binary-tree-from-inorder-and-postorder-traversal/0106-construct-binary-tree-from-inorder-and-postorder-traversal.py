# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildtrec(self,inorder,postorder):
        if inorder:
            root = TreeNode(postorder.pop())
            root_index = inorder.index(root.val)
            root.left = self.buildtrec(inorder[:root_index],postorder[:root_index])
            root.right = self.buildtrec(inorder[root_index+1:],postorder[root_index:])
            return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        n=len(inorder)
        if n==0:
            return None
        else:
            return self.buildtrec(inorder,postorder)
        