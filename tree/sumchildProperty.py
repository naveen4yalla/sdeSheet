class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 

def sumProperty(root):
    if root is None:
        return 
    sum = 0
    if root.left:
        sum = sum + root.left.val
    if root.right:
        sum = sum + root.right.val
        
    if sum < root.val:
        if root.left:
            root.left.val = root.val
        if root.right:
            root.right.val = root.val
    else:
        root.val = sum
    sumProperty(root.left)
    sumProperty(root.right)
    #recheck the root property
    total = 0
    if root.left:
        total = total + root.left.val
    if root.right:
        total = total + root.right.val
    if root.left or root.right:
        root.val = total
        
        




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)