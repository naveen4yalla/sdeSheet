class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 
def isSymmetric(root1,root2):
    if root1 is None or root2 is None:
        return root1  == root2
    return (root1.val == root2.val) and isSymmetric(root1.left,root2.right) and isSymmetric(root1.right,root2.left)
    