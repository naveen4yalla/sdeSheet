class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root) -> None:
       # prev = None
        self.flattenUtil(root)
        return self.prev
    def flattenUtil(self,root):
        if root is None:
                return 
        self.flattenUtil(root.right)
        self.flattenUtil(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
