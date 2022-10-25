class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 


def leftViewOfBinaryTree(root,level,result):
    if root == None: return
    if level == len(result):
        result.append(root.val)
    leftViewOfBinaryTree(root.left,level+1,result)
    leftViewOfBinaryTree(root.right,level+1,result)
def rightViewOfBinaryTree(root,level,result):
    if root == None: return
    if level == len(result):
        result.append(root.val)
    rightViewOfBinaryTree(root.right,level+1,result)
    rightViewOfBinaryTree(root.left,level+1,result)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6) 
result = []
leftViewOfBinaryTree(root,0,result)
print(result)
result = []
rightViewOfBinaryTree(root,0,result)
print(result)