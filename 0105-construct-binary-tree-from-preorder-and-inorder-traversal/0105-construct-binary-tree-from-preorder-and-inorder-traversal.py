# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildtrec(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(preorder.pop(0))
            root_index = inorder.index(root.val)
            root.left = self.buildtrec(preorder,inorder[:root_index])
            root.right = self.buildtrec(preorder,inorder[root_index+1:])
            return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        n=len(inorder)
        if n==0:
            return None
        else:
            return self.buildtrec(preorder,inorder)
    
        