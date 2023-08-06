class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root=TreeNode(val)
        else:
            self._insert(root,val)
        return root
    def _insert(self,root,val):
        if root.val>val:
            if root.left is not None:
                self._insert(root.left,val)
            else:
                root.left=TreeNode(val)
        else:
            if root.right is not None:
                self._insert(root.right,val)
            else:
                root.right=TreeNode(val)